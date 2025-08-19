from abc import ABC, abstractmethod

from src.coverage.coverage_data import CoverageData
from src.optimisation.configs.algorithm_config import AlgorithmConfig
from src.optimisation.configs.optimisation_config import OptimisationConfig
from src.project.target_project import TargetProject


class BaseOptimisation(ABC):
    def __init__(self, target_project: TargetProject,
                 algorithm_config: AlgorithmConfig,
                 optimisation_config: OptimisationConfig):
        super().__init__()
        self.coverage_data_list = target_project.coverage_data_list
        self.coverage_data_handler = target_project.coverage_data_handler
        self.initial_coverage_data = target_project.initial_coverage_data
        self.algorithm_config = algorithm_config
        self.optimisation_config = optimisation_config

    def objective_function(self, coverage_data: CoverageData) -> float:
        if coverage_data.coverage < self.optimisation_config.min_coverage:
            return float('-inf')

        coverage_fitness = coverage_data.coverage * self.optimisation_config.coverage_importance
        reduction_fitness = (self.initial_coverage_data.num_of_tests - coverage_data.num_of_tests) \
                            * self.optimisation_config.reduction_importance
        efficiency_fitness = (self.initial_coverage_data.exec_time / coverage_data.exec_time) \
                             * self.optimisation_config.efficiency_importance

        total_fitness = coverage_fitness + reduction_fitness + efficiency_fitness

        return total_fitness

    @abstractmethod
    def start_optimisation(self) -> CoverageData:
        raise NotImplementedError
