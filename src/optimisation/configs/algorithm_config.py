from typing import Union, NewType

from src.optimisation.configs.bayesian_config import BayesianConfig
from src.optimisation.configs.genetic_config import GeneticConfig
from src.optimisation.configs.random_config import RandomConfig

AlgorithmConfig = NewType('AlgorithmConfig', Union[GeneticConfig, RandomConfig, BayesianConfig, None])
