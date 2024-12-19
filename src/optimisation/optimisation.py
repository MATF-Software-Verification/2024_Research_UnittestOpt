from typing import Union

from src.coverage.python.python_coverage_data_handler import PythonCoverageDataHandler
from src.optimisation.algorithms.bayesian_optimisation import BayesianOptimisation
from src.optimisation.algorithms.bruteforce_optimisation import BruteforceOptimisation
from src.optimisation.algorithms.random_optimisation import RandomOptimisation
from src.optimisation.configs.genetic_config import GeneticConfig
from src.optimisation.configs.optimisation_config import OptimisationConfig
from src.optimisation.algorithms.genetic_optimisation import GeneticOptimisation


class Optimisation:
    def __init__(self, optimisation_type: Union['random', 'genetic', 'bayesian'],
                 optimisation_config: OptimisationConfig, algorithm_config: Union[GeneticConfig]):
        self.optimisation_type = optimisation_type
        self.optimisation_config = optimisation_config
        self.algorithm_config = algorithm_config

    def run(self, project_path):
        coverage_data_handler = PythonCoverageDataHandler(project_path=project_path)
        coverage_data_list = coverage_data_handler.get_coverage_data()
        if self.optimisation_type == 'random':
            optimisation = RandomOptimisation(coverage_data_list=coverage_data_list,
                                              coverage_data_handler=coverage_data_handler,
                                              algorithm_config=self.algorithm_config,
                                              optimisation_config=self.optimisation_config)
        elif self.optimisation_type == 'genetic':
            optimisation = GeneticOptimisation(coverage_data_list=coverage_data_list,
                                               coverage_data_handler=coverage_data_handler,
                                               algorithm_config=self.algorithm_config,
                                               optimisation_config=self.optimisation_config)
        elif self.optimisation_type == 'bayesian':
            optimisation = BayesianOptimisation(coverage_data_list=coverage_data_list,
                                               coverage_data_handler=coverage_data_handler,
                                               algorithm_config=self.algorithm_config,
                                               optimisation_config=self.optimisation_config)
        elif self.optimisation_type == 'bruteforce':
            optimisation = BruteforceOptimisation(coverage_data_list=coverage_data_list,
                                                coverage_data_handler=coverage_data_handler,
                                                algorithm_config=None,
                                                optimisation_config=self.optimisation_config)
        else:
            raise NotImplementedError

        results = optimisation.start_optimisation()
        return results
