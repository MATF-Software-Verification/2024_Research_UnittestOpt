from itertools import compress
from typing import List

import optuna
from optuna.samplers import TPESampler
from optuna.study import StudyDirection

from src.coverage.coverage_data import CoverageData
from src.optimisation.algorithms.base_optimisation import BaseOptimisation


class BayesianOptimisation(BaseOptimisation):

    def objective(self, trial: optuna.Trial):
        tests_subset_indicators = []
        for i in range(len(self.coverage_data_list)):
            indicator = trial.suggest_categorical(name='indicator_' + str(i), choices=[True, False])
            tests_subset_indicators.append(indicator)
        tests_subset = list(compress(self.coverage_data_list, tests_subset_indicators))
        coverage_data = self.coverage_data_handler.combine_coverage_data(tests_subset)
        return self.objective_function(coverage_data)

    def start_optimisation(self) -> List[CoverageData]:
        sampler = TPESampler(seed=self.algorithm_config.seed, n_startup_trials=self.algorithm_config.num_of_trials//3, multivariate=True, group=True)
        study = optuna.create_study(sampler=sampler,
                                    direction=StudyDirection.MAXIMIZE,
                                    study_name="Unittest optimisation")
        func = lambda trial: self.objective(trial)
        study.optimize(func,
                       n_trials=self.algorithm_config.num_of_trials)
        tests_subset_indicators = list(study.best_params.values())
        tests_subset = list(compress(self.coverage_data_list, tests_subset_indicators))
        coverage_data = self.coverage_data_handler.combine_coverage_data(tests_subset)
        return [coverage_data]
