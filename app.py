from src.coverage.python.python_coverage_data_handler import PythonCoverageDataHandler

handler = PythonCoverageDataHandler(project_path=r'C:\Users\pan3bg\Downloads\python-testing-101-master\python-testing-101-master\example-py-pytest')
coverage_data = handler.get_coverage_data()
total_coverage = handler.combine_coverage_data(coverage_data)
print(total_coverage)
