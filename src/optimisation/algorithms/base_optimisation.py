from abc import ABC, abstractmethod
from typing import List, Union

from src.coverage.coverage_data import CoverageData
from src.coverage.coverage_data_handler import CoverageDataHandler
from src.optimisation.configs.bayesian_config import BayesianConfig
from src.optimisation.configs.genetic_config import GeneticConfig
from src.optimisation.configs.optimisation_config import OptimisationConfig
from src.optimisation.configs.random_config import RandomConfig


class BaseOptimisation(ABC):
    def __init__(self, coverage_data_list: List[CoverageData], coverage_data_handler: CoverageDataHandler,
                 algorithm_config: Union[GeneticConfig, RandomConfig, BayesianConfig],
                 optimisation_config: OptimisationConfig):
        super().__init__()
        self.coverage_data_list = coverage_data_list
        self.coverage_data_handler = coverage_data_handler
        self.initial_tests_coverage_data = coverage_data_handler.combine_coverage_data(self.coverage_data_list)
        self.algorithm_config = algorithm_config
        self.optimisation_config = optimisation_config

    def objective_function(self, coverage_data: CoverageData) -> float:
        if coverage_data.coverage < self.optimisation_config.min_coverage:
            return float('-inf')

        coverage_fitness = coverage_data.coverage * self.optimisation_config.coverage_importance
        reduction_fitness = (self.initial_tests_coverage_data.num_of_tests - coverage_data.num_of_tests) \
                            * self.optimisation_config.reduction_importance
        efficiency_fitness = (self.initial_tests_coverage_data.exec_time / coverage_data.exec_time) \
                             * self.optimisation_config.efficiency_importance

        return coverage_fitness + reduction_fitness + efficiency_fitness

    @abstractmethod
    def start_optimisation(self) -> List[CoverageData]:
        raise NotImplementedError
