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
from src.utils.module_cache_manager import ModuleCacheManager

@pytest.fixture(scope="function", autouse=True)
def clear_modules_before_tests():
    test_dir = os.path.dirname(__file__)
    pytest_project_path = os.path.abspath(os.path.join(test_dir, '../data/test_projects/pytest_project'))
    unittest_project_path = os.path.abspath(os.path.join(test_dir, '../data/test_projects/unittest_project'))

    ModuleCacheManager.clear_all([pytest_project_path, unittest_project_path])


@pytest.fixture(scope="class")
def target_project_pytest():
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/test_projects/pytest_project'))
    return TargetProject(data_path)

@pytest.fixture(scope="class")
def target_project_unittest():
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/test_projects/unittest_project'))
    return TargetProject(data_path)

@pytest.fixture(scope="session")
def optimisation_config():
    return OptimisationConfig(
        optimisation_type='bruteforce',
        coverage_importance=1.0,
        reduction_importance=1.0,
        efficiency_importance=1.0,
        min_coverage=0.8
    )

@pytest.fixture(scope="class")
def bruteforce_result_pytest(target_project_pytest, optimisation_config):
    bruteforce_config = BruteforceConfig()
    bruteforce = BruteforceOptimisation(target_project_pytest, bruteforce_config, optimisation_config)
    return bruteforce.start_optimisation()

@pytest.fixture(scope="class")
def bruteforce_result_unittest(target_project_unittest, optimisation_config):
    bruteforce_config = BruteforceConfig()
    bruteforce = BruteforceOptimisation(target_project_unittest, bruteforce_config, optimisation_config)
    return bruteforce.start_optimisation()


class TestBruteforceFixedValues:

    def test_bruteforce_pytest_project_values(self, bruteforce_result_pytest):
        expected_coverage = 100.0
        expected_test_case_count = 3

        assert bruteforce_result_pytest.coverage == expected_coverage, f"Expected coverage {expected_coverage}, got {bruteforce_result_pytest.coverage}"
        assert len(
            bruteforce_result_pytest.test_cases) == expected_test_case_count, f"Expected {expected_test_case_count} test cases, got {len(bruteforce_result_pytest.test_cases)}"
        assert bruteforce_result_pytest.exec_time > 0, "Execution time should be greater than 0"

    def test_bruteforce_unittest_project_values(self, bruteforce_result_unittest):
        expected_coverage = 100.0
        expected_test_case_count = 3

        assert bruteforce_result_unittest.coverage == expected_coverage, f"Expected coverage {expected_coverage}, got {bruteforce_result_unittest.coverage}"
        assert len(
            bruteforce_result_unittest.test_cases) == expected_test_case_count, f"Expected {expected_test_case_count} test cases, got {len(bruteforce_result_unittest.test_cases)}"
        assert bruteforce_result_unittest.exec_time > 0, "Execution time should be greater than 0"

    def test_bruteforce_results_consistency(self, bruteforce_result_pytest, bruteforce_result_unittest):
        assert bruteforce_result_pytest.coverage == bruteforce_result_unittest.coverage, "Both projects should achieve same coverage"
        assert len(bruteforce_result_pytest.test_cases) == len(
            bruteforce_result_unittest.test_cases), "Both projects should have same number of optimal test cases"


class TestBayesianVsBruteforcePytest:
    @pytest.fixture(scope="class")
    def bayesian_config(self):
        return BayesianConfig(seed=42, num_of_trials=100)

    @pytest.fixture(scope="class")
    def bayesian_result(self, target_project_pytest, optimisation_config, bayesian_config):
        bayesian = BayesianOptimisation(target_project_pytest, bayesian_config, optimisation_config)
        return bayesian.start_optimisation()

    def test_coverage_matches(self, bruteforce_result_pytest, bayesian_result):
        assert bruteforce_result_pytest.coverage == bayesian_result.coverage, "Coverage values do not match"

    def test_exec_time_matches(self, bruteforce_result_pytest, bayesian_result):
        assert bruteforce_result_pytest.exec_time == bayesian_result.exec_time, "Execution times do not match"

    def test_test_cases_match(self, bruteforce_result_pytest, bayesian_result):
        assert len(bruteforce_result_pytest.test_cases) == len(bayesian_result.test_cases), "Test cases length do not match"

class TestGeneticVsBruteforcePytest:
    @pytest.fixture(scope="class")
    def genetic_config(self):
        return GeneticConfig(
            population_size=10,
            num_of_iterations=50,
            elitism_factor=0.2,
            mutation_factor=0.05,
            seed=42
        )

    @pytest.fixture(scope="class")
    def genetic_result(self, target_project_pytest, optimisation_config, genetic_config):
        genetic = GeneticOptimisation(target_project_pytest, genetic_config, optimisation_config)
        return genetic.start_optimisation()

    def test_coverage_matches(self, bruteforce_result_pytest, genetic_result):
        assert bruteforce_result_pytest.coverage == genetic_result.coverage, "Coverage values do not match"

    def test_exec_time_matches(self, bruteforce_result_pytest, genetic_result):
        assert bruteforce_result_pytest.exec_time == genetic_result.exec_time, "Execution times do not match"

    def test_test_cases_match(self, bruteforce_result_pytest, genetic_result):
        assert len(bruteforce_result_pytest.test_cases) == len(genetic_result.test_cases), "Test cases length do not match"

class TestRandomVsBruteforcePytest:
    @pytest.fixture(scope="class")
    def random_config(self):
        return RandomConfig(seed=42, num_of_trials=100, test_inclusion_prob=0.7)

    @pytest.fixture(scope="class")
    def random_result(self, target_project_pytest, optimisation_config, random_config):
        random = RandomOptimisation(target_project_pytest, random_config, optimisation_config)
        return random.start_optimisation()

    def test_coverage_matches(self, bruteforce_result_pytest, random_result):
        assert bruteforce_result_pytest.coverage == random_result.coverage, "Coverage values do not match"

    def test_exec_time_matches(self, bruteforce_result_pytest, random_result):
        assert bruteforce_result_pytest.exec_time == random_result.exec_time, "Execution times do not match"

    def test_test_cases_match(self, bruteforce_result_pytest, random_result):
        assert len(bruteforce_result_pytest.test_cases) == len(random_result.test_cases), "Test cases length do not match"

# Test classes for unittest project
class TestBayesianVsBruteforceUnittest:
    @pytest.fixture(scope="class")
    def bayesian_config(self):
        return BayesianConfig(seed=42, num_of_trials=100)

    @pytest.fixture(scope="class")
    def bayesian_result_unittest(self, target_project_unittest, optimisation_config, bayesian_config):
        bayesian = BayesianOptimisation(target_project_unittest, bayesian_config, optimisation_config)
        return bayesian.start_optimisation()

    def test_coverage_matches(self, bruteforce_result_unittest, bayesian_result_unittest):
        assert bruteforce_result_unittest.coverage == bayesian_result_unittest.coverage, "Coverage values do not match for unittest project"

    def test_exec_time_matches(self, bruteforce_result_unittest, bayesian_result_unittest):
        assert bruteforce_result_unittest.exec_time == bayesian_result_unittest.exec_time, "Execution times do not match for unittest project"

    def test_test_cases_match(self, bruteforce_result_unittest, bayesian_result_unittest):
        assert len(bruteforce_result_unittest.test_cases) == len(bayesian_result_unittest.test_cases), "Test cases length do not match for unittest project"

class TestGeneticVsBruteforceUnittest:
    @pytest.fixture(scope="class")
    def genetic_config(self):
        return GeneticConfig(
            population_size=10,
            num_of_iterations=50,
            elitism_factor=0.1,
            mutation_factor=0.05,
            seed=42
        )

    @pytest.fixture(scope="class")
    def genetic_result_unittest(self, target_project_unittest, optimisation_config, genetic_config):
        genetic = GeneticOptimisation(target_project_unittest, genetic_config, optimisation_config)
        return genetic.start_optimisation()

    def test_coverage_matches(self, bruteforce_result_unittest, genetic_result_unittest):
        assert bruteforce_result_unittest.coverage == genetic_result_unittest.coverage, "Coverage values do not match for unittest project"

    def test_exec_time_matches(self, bruteforce_result_unittest, genetic_result_unittest):
        assert bruteforce_result_unittest.exec_time == genetic_result_unittest.exec_time, "Execution times do not match for unittest project"

    def test_test_cases_match(self, bruteforce_result_unittest, genetic_result_unittest):
        assert len(bruteforce_result_unittest.test_cases) == len(genetic_result_unittest.test_cases), "Test cases length do not match for unittest project"

class TestRandomVsBruteforceUnittest:
    @pytest.fixture(scope="class")
    def random_config(self):
        return RandomConfig(seed=42, num_of_trials=100, test_inclusion_prob=0.7)

    @pytest.fixture(scope="class")
    def random_result_unittest(self, target_project_unittest, optimisation_config, random_config):
        random = RandomOptimisation(target_project_unittest, random_config, optimisation_config)
        return random.start_optimisation()

    def test_coverage_matches(self, bruteforce_result_unittest, random_result_unittest):
        assert bruteforce_result_unittest.coverage == random_result_unittest.coverage, "Coverage values do not match for unittest project"

    def test_exec_time_matches(self, bruteforce_result_unittest, random_result_unittest):
        assert bruteforce_result_unittest.exec_time == random_result_unittest.exec_time, "Execution times do not match for unittest project"

    def test_test_cases_match(self, bruteforce_result_unittest, random_result_unittest):
        assert len(bruteforce_result_unittest.test_cases) == len(random_result_unittest.test_cases), "Test cases length do not match for unittest project"
