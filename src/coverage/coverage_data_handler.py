from abc import ABC, abstractmethod
from typing import List

from src.coverage.coverage_data import CoverageData


class CoverageDataHandler(ABC):
    def __init__(self, project_path: str):
        super().__init__()
        self.project_path = project_path
        self.coverage_data_files_path = 'tmp/coverage_data/'

    @abstractmethod
    def collect_test_cases(self) -> List[str]:
        raise NotImplementedError

    @abstractmethod
    def get_coverage_data(self) -> List[CoverageData]:
        raise NotImplementedError

    @abstractmethod
    def combine_coverage_data(self, coverage_data_list: List[CoverageData]) -> CoverageData:
        raise NotImplementedError
