from typing import List


class CoverageData:
    def __init__(self, id: str, coverage: float, exec_time: float, test_cases: List[str]):
        self.id = id
        self.coverage = coverage
        self.exec_time = exec_time
        self.test_cases = test_cases
        self.num_of_tests = len(self.test_cases)

    def __str__(self):
        return f'Number of tests executed: {self.num_of_tests}\nCoverage is {self.coverage}% \nExecution time is {self.exec_time}s\n'
