class CoverageData:
    def __init__(self, id: str, coverage: float, exec_time: float, num_of_tests: int):
        self.id = id
        self.coverage = coverage
        self.exec_time = exec_time
        self.num_of_tests = num_of_tests

    def __str__(self):
        return f'Number of tests executed: {self.num_of_tests}\nCoverage is {self.coverage}% \nExecution time is {self.exec_time}s\n'
