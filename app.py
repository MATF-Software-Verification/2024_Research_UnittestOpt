import numpy as np

from src.optimisation.configs.bayesian_config import BayesianConfig
from src.optimisation.configs.genetic_config import GeneticConfig
from src.optimisation.configs.optimisation_config import OptimisationConfig
from src.optimisation.configs.random_config import RandomConfig
from src.optimisation.optimisation import Optimisation

np.random.seed(42)

random_config = RandomConfig(seed=42, num_of_trials=30)
genetic_config = GeneticConfig(mutation_factor=0.01, num_of_iterations=10, population_size=9, elitism_factor=0.3)
bayesian_config = BayesianConfig(seed=42, num_of_trials=50)
optimisation_config = OptimisationConfig(coverage_importance=1, reduction_importance=0.2, efficiency_importance=0.1, min_coverage=0.45)

optimisation = Optimisation(optimisation_type='bayesian', algorithm_config=bayesian_config, optimisation_config=optimisation_config)
results = optimisation.run(project_path=r'C:\Users\pan3bg\Downloads\python-testing-101-master\python-testing-101-master\example-py-pytest')
for res in results[:3]:
    print(res)