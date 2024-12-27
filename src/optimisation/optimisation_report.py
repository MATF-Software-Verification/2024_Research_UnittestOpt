import json


class OptimisationReport:
    def __init__(self, start_time, end_time, coverage_data, target_project, optimisation_config, algorithm_config):
        self.start_time = start_time
        self.end_time = end_time
        self.duration = self.end_time - self.start_time
        self.coverage_data = coverage_data
        self.target_project = target_project
        self.optimisation_config = optimisation_config
        self.algorithm_config = algorithm_config

    def export(self, path):
        excluded_test_cases = list(
            set(self.target_project.initial_coverage_data.test_cases) - set(self.coverage_data.test_cases))
        report = {
            'project_path': self.target_project.project_path,
            'num_of_all_test_cases_detected': len(self.target_project.coverage_data_list),
            'all_test_cases_detected': self.target_project.initial_coverage_data.test_cases,
            'all_test_cases_exec_time': self.target_project.initial_coverage_data.exec_time,
            'all_test_cases_coverage': self.target_project.initial_coverage_data.coverage,
            'optimisation_start_time': str(self.start_time),
            'optimisation_end_time': str(self.end_time),
            'optimisation_duration': str(self.duration),
            'optimisation_config': vars(self.optimisation_config),
            'algorithm_config': vars(self.algorithm_config),
            'num_of_optimal_test_cases': self.coverage_data.num_of_tests,
            'optimal_test_cases': self.coverage_data.test_cases,
            'optimal_test_cases_coverage': self.coverage_data.coverage,
            'optimal_exec_time': self.coverage_data.exec_time,
            'excluded_test_cases': excluded_test_cases,
            'num_of_excluded_test_cases': len(excluded_test_cases),
            'coverage_loss': self.target_project.initial_coverage_data.coverage - self.coverage_data.coverage,
            'exec_time_gain': self.target_project.initial_coverage_data.exec_time - self.coverage_data.exec_time
        }

        with open(path + '/optimisation_report_' + self.start_time.strftime("%Y_%m_%d-%I_%M_%S_%p") + '.json',
                  'w') as fp:
            json.dump(report, fp, indent="\t")
