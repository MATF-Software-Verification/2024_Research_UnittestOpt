from itertools import compress
from typing import List

import numpy as np

from src.coverage.coverage_data import CoverageData
from src.optimisation.algorithms.base_optimisation import BaseOptimisation


class RandomOptimisation(BaseOptimisation):

    def start_optimisation(self) -> List[CoverageData]:
        np.random.seed(self.algorithm_config.seed)
        results = []
        for i in range(self.algorithm_config.num_of_trials):
            tests_subset_indicators = np.random.choice([True, False], p=[self.algorithm_config.test_inclusion_prob,
                                                                         1 - self.algorithm_config.test_inclusion_prob],
                                                       size=len(self.coverage_data_list))
            tests_subset = list(compress(self.coverage_data_list, tests_subset_indicators))
            coverage_data = self.coverage_data_handler.combine_coverage_data(tests_subset)
            results.append(coverage_data)
        return max(results, key=self.objective_function)
