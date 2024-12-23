from src.coverage.python.python_coverage_data_handler import PythonCoverageDataHandler


class TargetProject:
    def __init__(self, project_path: str):
        self.project_path = project_path
        self.coverage_data_handler = PythonCoverageDataHandler(project_path=project_path)
        self.coverage_data_list = self.coverage_data_handler.get_coverage_data()
        if len(self.coverage_data_list) > 1:
            self.initial_coverage_data = self.coverage_data_handler.combine_coverage_data(self.coverage_data_list)
            self.valid_project = True
        else:
            self.initial_coverage_data = None
            self.valid_project = False
