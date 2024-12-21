class GeneticConfig:
    def __init__(self, population_size: int, num_of_iterations, elitism_factor: float, mutation_factor: float):
        self.population_size = population_size
        self.num_of_iterations = num_of_iterations
        self.elitism_factor = elitism_factor
        self.mutation_factor = mutation_factor
