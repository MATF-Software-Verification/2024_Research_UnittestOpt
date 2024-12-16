import numpy as np
from src.coverage.python.python_coverage_data_handler import PythonCoverageDataHandler
from src.optimisation.configs.GeneticConfig import GeneticConfig
from src.optimisation.configs.OptimisationConfig import OptimisationConfig
from src.optimisation.genetic import Genetic

np.random.seed(42)
handler = PythonCoverageDataHandler(project_path=r'C:\Users\pan3bg\Downloads\python-testing-101-master\python-testing-101-master\example-py-pytest')
coverage_data = handler.get_coverage_data()
total_coverage = handler.combine_coverage_data(coverage_data)

genetic_config = GeneticConfig(mutation_factor=0.01, num_of_iterations=30, population_size=9, elitism_factor=0.3)
optimisation_config = OptimisationConfig(coverage_importance=1, reduction_importance=0.2, efficiency_importance=0.1, min_coverage=0.45)

genetic = Genetic(coverage_data, handler, genetic_config, optimisation_config)
final_pop = genetic.start_evolution()[:3]
print(total_coverage)
for ind in final_pop:
    print(ind.coverage_data)
    print(ind.fitness)
    print('-----------------------------------------------\n')
