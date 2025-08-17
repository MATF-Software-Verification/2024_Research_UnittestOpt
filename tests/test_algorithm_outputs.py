import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.optimisation.algorithms.bruteforce_optimisation import BruteforceOptimisation
from src.optimisation.algorithms.bayesian_optimisation import BayesianOptimisation
from src.optimisation.algorithms.genetic_optimisation import GeneticOptimisation
from src.optimisation.algorithms.random_optimisation import RandomOptimisation
from src.optimisation.configs.optimisation_config import OptimisationConfig
from src.project.target_project import TargetProject
from src.optimisation.configs.random_config import RandomConfig
from src.optimisation.configs.bayesian_config import BayesianConfig
from src.optimisation.configs.bruteforce_config import BruteforceConfig
from src.optimisation.configs.genetic_config import GeneticConfig

# Fixtures to set up resources that will be shared across tests
@pytest.fixture(scope="session")
def target_project():
    """Fixture to load test project data once for the entire test session"""
    print("Loading target project...")
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/test_projects'))
    return TargetProject(data_path)

@pytest.fixture(scope="session")
def optimisation_config():
    """Fixture for the optimization configuration that is shared across all tests"""
    return OptimisationConfig(
        optimisation_type='bruteforce',
        coverage_importance=1.0,
        reduction_importance=1.0,
        efficiency_importance=1.0,
        min_coverage=0.8
    )

@pytest.fixture(scope="session")
def bruteforce_result(target_project, optimisation_config):
    """Fixture to calculate bruteforce results once and reuse them across tests"""
    print("Calculating bruteforce results (this will be done only once)...")
    bruteforce_config = BruteforceConfig()
    bruteforce = BruteforceOptimisation(target_project, bruteforce_config, optimisation_config)
    return bruteforce.start_optimisation()

# Test classes for each algorithm
class TestBayesianVsBruteforce:
    @pytest.fixture(scope="class")
    def bayesian_config(self):
        return BayesianConfig(seed=42, num_of_trials=30)

    @pytest.fixture(scope="class")
    def bayesian_result(self, target_project, optimisation_config, bayesian_config):
        bayesian = BayesianOptimisation(target_project, bayesian_config, optimisation_config)
        return bayesian.start_optimisation()

    def test_coverage_matches(self, bruteforce_result, bayesian_result):
        assert bruteforce_result.coverage == bayesian_result.coverage, "Coverage values do not match"

    def test_exec_time_matches(self, bruteforce_result, bayesian_result):
        assert bruteforce_result.exec_time == bayesian_result.exec_time, "Execution times do not match"

    def test_test_cases_match(self, bruteforce_result, bayesian_result):
        assert bruteforce_result.test_cases == bayesian_result.test_cases, "Test cases do not match"

class TestGeneticVsBruteforce:
    @pytest.fixture(scope="class")
    def genetic_config(self):
        return GeneticConfig(
            population_size=10,
            num_of_iterations=30,
            elitism_factor=0.1,
            mutation_factor=0.05,
            seed=42
        )

    @pytest.fixture(scope="class")
    def genetic_result(self, target_project, optimisation_config, genetic_config):
        genetic = GeneticOptimisation(target_project, genetic_config, optimisation_config)
        return genetic.start_optimisation()

    def test_coverage_matches(self, bruteforce_result, genetic_result):
        assert bruteforce_result.coverage == genetic_result.coverage, "Coverage values do not match"

    def test_exec_time_matches(self, bruteforce_result, genetic_result):
        assert bruteforce_result.exec_time == genetic_result.exec_time, "Execution times do not match"

    def test_test_cases_match(self, bruteforce_result, genetic_result):
        assert bruteforce_result.test_cases == genetic_result.test_cases, "Test cases do not match"

class TestRandomVsBruteforce:
    @pytest.fixture(scope="class")
    def random_config(self):
        return RandomConfig(seed=42, num_of_trials=100, test_inclusion_prob=0.8)

    @pytest.fixture(scope="class")
    def random_result(self, target_project, optimisation_config, random_config):
        random = RandomOptimisation(target_project, random_config, optimisation_config)
        return random.start_optimisation()

    def test_coverage_matches(self, bruteforce_result, random_result):
        assert bruteforce_result.coverage == random_result.coverage, "Coverage values do not match"

    def test_exec_time_matches(self, bruteforce_result, random_result):
        assert bruteforce_result.exec_time == random_result.exec_time, "Execution times do not match"

    def test_test_cases_match(self, bruteforce_result, random_result):
        assert bruteforce_result.test_cases == random_result.test_cases, "Test cases do not match"
