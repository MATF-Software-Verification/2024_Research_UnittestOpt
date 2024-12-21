import itertools
from typing import List

import numpy as np

from src.coverage.coverage_data import CoverageData
from src.optimisation.algorithms.base_optimisation import BaseOptimisation


class BruteforceOptimisation(BaseOptimisation):

    def start_optimisation(self) -> List[CoverageData]:
        tests_subset_indicators = np.ones(len(self.coverage_data_list), dtype=bool)
        tests_subset = list(itertools.compress(self.coverage_data_list, tests_subset_indicators))
        current_best = self.coverage_data_handler.combine_coverage_data(tests_subset)

        all_indicators = itertools.product([True, False], repeat=len(self.coverage_data_list))
        for idx, tests_subset_indicators in enumerate(all_indicators):
            tests_subset = list(itertools.compress(self.coverage_data_list, tests_subset_indicators))
            coverage_data = self.coverage_data_handler.combine_coverage_data(tests_subset)
            if self.objective_function(coverage_data) > self.objective_function(current_best):
                current_best = coverage_data
            if idx > 100:
                break

        return [current_best]
