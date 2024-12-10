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
        self.coverage_data = self.get_coverage_data()
        self.fitness = self.fitness_function()

    def __str__(self):
        return str(self.current_tests_subset)

    def __lt__(self, other):
        return self.fitness < other.fitness

    def get_coverage_data(self):
       pass

    def fitness_function(self):
        if self.min_coverage and self.coverage_data.coverage < self.min_coverage:
            return float('-inf')

        coverage_fitness = self.coverage_data.coverage * self.coverage_importance_coefficient
        reduction_fitness = (self.initial_tests_coverage_data.num_of_tests - self.coverage_data.num_of_tests)\
                            *self.reduction_importance_coefficient
        efficiency_fitness = (self.initial_tests_coverage_data.execution_time / self.coverage_data.execution_time) \
                             *self.efficiency_importance_coefficient

        return  coverage_fitness + reduction_fitness + efficiency_fitness

