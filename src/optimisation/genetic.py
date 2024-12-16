import numpy as np
from src.coverage_handler.coverage import get_coverage_data


class Individual:
    def __init__(self, current_tests_subset,
                 initial_tests_coverage_data,
                 reduction_importance_coefficient = 1,
                 coverage_importance_coefficient = 1,
                 efficiency_importance_coefficient = 1,
                 min_coverage = None):
        self.current_tests_subset = current_tests_subset
        self.initial_tests_coverage_data = initial_tests_coverage_data
        self.reduction_importance_coefficient = reduction_importance_coefficient
        self.coverage_importance_coefficient = coverage_importance_coefficient
        self.efficiency_importance_coefficient = efficiency_importance_coefficient
        self.min_coverage = min_coverage
        self.coverage_data = get_coverage_data(self.current_tests_subset)
        self.fitness = self.fitness_function()

    def __str__(self):
        return str(self.current_tests_subset)

    def __lt__(self, other):
        return self.fitness < other.fitness

    def fitness_function(self):
        if self.min_coverage and self.coverage_data.coverage < self.min_coverage:
            return float('-inf')

        coverage_fitness = self.coverage_data.coverage * self.coverage_importance_coefficient
        reduction_fitness = (self.initial_tests_coverage_data.num_of_tests - self.coverage_data.num_of_tests)\
                            *self.reduction_importance_coefficient
        efficiency_fitness = (self.initial_tests_coverage_data.execution_time / self.coverage_data.execution_time) \
                             *self.efficiency_importance_coefficient

        return  coverage_fitness + reduction_fitness + efficiency_fitness


class Genetic:

    def __init__(self, tests_set):
        self.tests_set = tests_set
        self.initial_tests_coverage_data = get_coverage_data(self.tests_set)

    def generate_init_population(self, population_size):
        init_population = []
        for i in range (0, population_size):
            pass
        return init_population

    def selection(self, population):
        return population[np.random.randint(len(population))]

    def crossover(self, parent_1, parent_2):
        pass

    def mutation(self, individual, mutation_factor):
        coloring = individual.coloring
        mutated_individual = individual
        for test in individual.current_tests_subset:
            if np.random.uniform() > mutation_factor:
                continue
            
            mutated_individual = Individual( )
        return mutated_individual
    def start_evolution(self,population_size, num_of_iterations, mutation_factor, elitism_factor):
        population = self.generate_init_population(population_size)
        new_population = population.copy()
        num_of_executed_iterations = 0
        for iteration in range(0, num_of_iterations):
            population.sort(reverse=True)
            for i in range(0, int(population_size*elitism_factor)):
                new_population[i] = population[i]
            for i in range(int(population_size*elitism_factor), population_size-1, 2):
                parent_1 = self.selection(population)
                parent_2 = self.selection(population)
                [child_1, child_2] = self.crossover(parent_1, parent_2)
                child_1 = self.mutation(child_1, mutation_factor)
                child_2 = self.mutation(child_2, mutation_factor)
                new_population[i] = child_1
                new_population[i+1] = child_2
            population = new_population.copy()
            num_of_executed_iterations += 1
        population.sort(reverse=True)
        return [population, num_of_executed_iterations]