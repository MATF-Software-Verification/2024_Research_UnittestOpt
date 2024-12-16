class CoverageData:
    def __init__(self, id:str, coverage:float, exec_time:float):
        self.id = id
        self.coverage = coverage
        self.exec_time = exec_time

    def __str__(self):
        return f'Coverage is {self.coverage}% \nExecution time is {self.exec_time}s\n'
