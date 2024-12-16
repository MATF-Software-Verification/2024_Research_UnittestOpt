from itertools import compress
from typing import List, Tuple

import numpy as np

from src.coverage.coverage_data import CoverageData
from src.coverage.coverage_data_handler import CoverageDataHandler
from src.optimisation.configs import GeneticConfig, OptimisationConfig


class Individual:
    def __init__(self, coverage_data_list: List[CoverageData],
                 tests_subset_indicators: List[int],
                 coverage_data_handler: CoverageDataHandler,
                 optimisation_config: OptimisationConfig
                 ):
        self.coverage_data_list = coverage_data_list
        self.tests_subset_indicators = tests_subset_indicators
        self.tests_subset = list(compress(self.coverage_data_list, self.tests_subset_indicators))
        self.coverage_data_handler = coverage_data_handler
        self.optimisation_config = optimisation_config

        self.coverage_data = self.coverage_data_handler.combine_coverage_data(self.tests_subset) if len(self.tests_subset) > 1 else self.tests_subset[0]
        self.initial_tests_coverage_data = self.coverage_data_handler.combine_coverage_data(self.coverage_data_list)
        self.fitness = self.fitness_function()

    def __str__(self):
        return str(self.current_tests_subset)

    def __lt__(self, other):
        return self.fitness < other.fitness

    def fitness_function(self) -> float:
        if self.coverage_data.coverage < self.optimisation_config.min_coverage:
            return float('-inf')

        coverage_fitness = self.coverage_data.coverage * self.optimisation_config.coverage_importance
        reduction_fitness = (self.initial_tests_coverage_data.num_of_tests - self.coverage_data.num_of_tests) \
                            * self.optimisation_config.reduction_importance
        efficiency_fitness = (self.initial_tests_coverage_data.exec_time / self.coverage_data.exec_time) \
                             * self.optimisation_config.efficiency_importance

        return coverage_fitness + reduction_fitness + efficiency_fitness


class Genetic:

    def __init__(self, coverage_data_list: List[CoverageData], coverage_data_handler: CoverageDataHandler,
                 genetic_config: GeneticConfig, optimisation_config: OptimisationConfig):
        self.coverage_data_list = coverage_data_list
        self.coverage_data_handler = coverage_data_handler
        self.initial_tests_coverage_data = coverage_data_handler.combine_coverage_data(self.coverage_data_list)
        self.genetic_config = genetic_config
        self.optimisation_config = optimisation_config

    def generate_init_population(self, population_size: int) -> List[Individual]:
        all_tests_indicators = np.ones(len(self.coverage_data_list), dtype=bool)
        init_population = [Individual(self.coverage_data_list, all_tests_indicators, self.coverage_data_handler, self.optimisation_config)]

        for i in range(0, population_size - 1):
            tests_subset_indicators = np.random.choice([False, True], size=len(self.coverage_data_list))
            current_individual = Individual(self.coverage_data_list, tests_subset_indicators,
                                            self.coverage_data_handler, self.optimisation_config)
            init_population.append(current_individual)
        return init_population

    def selection(self, population):
        return population[np.random.randint(len(population))]

    def crossover(self, parent_1: Individual, parent_2: Individual) -> Tuple[Individual,Individual]:
        child_1_indicators = []
        child_2_indicators = []
        while not any(child_1_indicators) and not any(child_2_indicators):
            for i in range(len(parent_1.tests_subset_indicators)):
                if np.random.uniform() > self.genetic_config.mutation_factor:
                    child_1_indicators.append(parent_1.tests_subset_indicators[i])
                    child_2_indicators.append(parent_2.tests_subset_indicators[i])
                else:
                    child_1_indicators.append(parent_2.tests_subset_indicators[i])
                    child_2_indicators.append(parent_1.tests_subset_indicators[i])
        child_1 = Individual(self.coverage_data_list, child_1_indicators, self.coverage_data_handler, self.optimisation_config)
        child_2 = Individual(self.coverage_data_list, child_2_indicators, self.coverage_data_handler, self.optimisation_config)
        return child_1, child_2

    def mutation(self, individual: Individual) -> Individual:
        mutated_indicators = []
        while not any(mutated_indicators):
            for indicator in individual.tests_subset_indicators:
                if np.random.uniform() < self.genetic_config.mutation_factor:
                    indicator = not indicator
                mutated_indicators.append(indicator)
        mutated_individual = Individual(self.coverage_data_list, mutated_indicators, self.coverage_data_handler, self.optimisation_config)
        return mutated_individual

    def start_evolution(self) -> List[Individual]:
        population = self.generate_init_population(self.genetic_config.population_size)
        new_population = population.copy()
        num_of_executed_iterations = 0
        for iteration in range(0, self.genetic_config.num_of_iterations):
            population.sort(reverse=True)
            elit_population_size = int(self.genetic_config.population_size * self.genetic_config.elitism_factor)
            for i in range(0, elit_population_size):
                new_population[i] = population[i]
            for i in range(elit_population_size, self.genetic_config.population_size - 1, 2):
                parent_1 = self.selection(population)
                parent_2 = self.selection(population)
                child_1, child_2 = self.crossover(parent_1, parent_2)
                child_1 = self.mutation(child_1)
                child_2 = self.mutation(child_2)
                new_population[i] = child_1
                new_population[i + 1] = child_2
            population = new_population.copy()
            num_of_executed_iterations += 1
        population.sort(reverse=True)
        return population
