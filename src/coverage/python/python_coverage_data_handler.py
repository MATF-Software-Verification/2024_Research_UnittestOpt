import io
import itertools
import os
import sys
from timeit import default_timer as timer
from typing import List

import coverage
import pytest

from src.coverage.coverage_data import CoverageData
from src.coverage.coverage_data_handler import CoverageDataHandler


class PythonCoverageDataHandler(CoverageDataHandler):
    def collect_test_cases(self) -> List[str]:
        cwd = os.getcwd()
        os.chdir(self.project_path)
        sys.path.insert(0, self.project_path)
        test_cases_collection_plugin = TestCasesCollectionPlugin()
        pytest.main(['--co', '-q', '-s'], plugins=[test_cases_collection_plugin])
        os.chdir(cwd)
        return test_cases_collection_plugin.collected

    def get_coverage_data(self) -> List[CoverageData]:
        coverage_data = []
        test_cases = self.collect_test_cases()
        sys.path.insert(0, self.project_path)
        for idx, test_case in enumerate(test_cases):
            coverage_data_file = self.coverage_data_files_path + 'data_file_' + str(idx)
            cov = coverage.Coverage(data_file=coverage_data_file, messages=False)
            start = timer()
            cov.start()
            pytest.main(['-x', self.project_path + '/' + test_case])
            cov.stop()
            cov.save()
            end = timer()
            coverage_data.append(
                CoverageData(str(idx), round(cov.report(file=io.StringIO()), 2), round(end - start, 2),
                             test_cases=[test_case]))
        return coverage_data

    def combine_coverage_data(self, coverage_data_list: List[CoverageData]) -> CoverageData:
        if len(coverage_data_list) == 0:
            coverage_data = CoverageData(id='empty', coverage=0,
                                         exec_time=float('inf'), test_cases=[])
        elif len(coverage_data_list) == 1:
            coverage_data = coverage_data_list.pop()
        else:
            data_paths = list(map(lambda cd: self.coverage_data_files_path + 'data_file_' + cd.id, coverage_data_list))
            cov = coverage.Coverage(messages=False)
            cov.combine(data_paths=data_paths, keep=True)
            exec_time = sum(list(map(lambda cd: cd.exec_time, coverage_data_list)))
            id = '_'.join(list(map(lambda cd: cd.id, coverage_data_list)))
            coverage_data = CoverageData(id=id, coverage=round(cov.report(file=io.StringIO()), 2),
                                         exec_time=round(exec_time, 2), test_cases=list(
                    itertools.chain.from_iterable(map(lambda el: el.test_cases, coverage_data_list))))
            cov.erase()
        return coverage_data


class TestCasesCollectionPlugin:
    def __init__(self):
        self.collected = []

    def pytest_collection_modifyitems(self, items):
        for item in items:
            self.collected.append(item.nodeid)
