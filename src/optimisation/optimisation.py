from src.optimisation.algorithms.bayesian_optimisation import BayesianOptimisation
from src.optimisation.algorithms.bruteforce_optimisation import BruteforceOptimisation
from src.optimisation.algorithms.genetic_optimisation import GeneticOptimisation
from src.optimisation.algorithms.random_optimisation import RandomOptimisation
from src.optimisation.configs.algorithm_config import AlgorithmConfig
from src.optimisation.configs.optimisation_config import OptimisationConfig
from src.optimisation.optimisation_report import OptimisationReport
from src.project.target_project import TargetProject


class Optimisation:
    def __init__(self, target_project: TargetProject,
                 optimisation_config: OptimisationConfig, algorithm_config: AlgorithmConfig):
        self.target_project = target_project
        self.optimisation_config = optimisation_config
        self.algorithm_config = algorithm_config

    def run(self) -> OptimisationReport:
        if self.optimisation_config.optimisation_type == 'random':
            optimisation = RandomOptimisation(target_project=self.target_project,
                                              algorithm_config=self.algorithm_config,
                                              optimisation_config=self.optimisation_config)
        elif self.optimisation_config.optimisation_type == 'genetic':
            optimisation = GeneticOptimisation(target_project=self.target_project,
                                               algorithm_config=self.algorithm_config,
                                               optimisation_config=self.optimisation_config)
        elif self.optimisation_config.optimisation_type == 'bayesian':
            optimisation = BayesianOptimisation(target_project=self.target_project,
                                                algorithm_config=self.algorithm_config,
                                                optimisation_config=self.optimisation_config)
        elif self.optimisation_config.optimisation_type == 'bruteforce':
            optimisation = BruteforceOptimisation(target_project=self.target_project,
                                                  algorithm_config=None,
                                                  optimisation_config=self.optimisation_config)
        else:
            raise NotImplementedError

        results = optimisation.start_optimisation()
        return OptimisationReport()
