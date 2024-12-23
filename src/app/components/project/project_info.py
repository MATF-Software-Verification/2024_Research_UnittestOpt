import customtkinter

from src.app.components.custom_component import CustomComponent
from src.app.components.frame_title import FrameTitle
from src.project.target_project import TargetProject


class ProjectInfo(CustomComponent):

    def __init__(self, root: customtkinter.CTk):
        self.frame = None
        self.target_project = None
        self.project_path_variable = customtkinter.StringVar(value='None')
        self.project_num_tests_variable = customtkinter.StringVar(value='Number of Tests: 0')
        self.project_coverage_variable = customtkinter.StringVar(value='Project Coverage: 0%')
        self.project_exec_time_variable = customtkinter.StringVar(value='Tests Execution Time: 0s')
        super().__init__(root)

    def layout_elements(self, root: customtkinter.CTk):
        self.frame = customtkinter.CTkFrame(root, bg_color='transparent', fg_color='transparent', border_color='grey',
                                            border_width=2)
        self.frame.grid_propagate(False)
        self.frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.frame.grid_rowconfigure((0, 1, 2), weight=1)

        title = FrameTitle(self.frame, text='LOADED PROJECT INFO')
        title.grid(row=0, column=0, columnspan=3)

        project_path_label = customtkinter.CTkLabel(self.frame, textvariable=self.project_path_variable)
        project_path_label.grid(row=1, column=0, columnspan=3, sticky='we', padx=10)

        project_num_tests_label = customtkinter.CTkLabel(self.frame, textvariable=self.project_num_tests_variable)
        project_num_tests_label.grid(row=2, column=0, sticky='we', padx=10)

        project_coverage_label = customtkinter.CTkLabel(self.frame, textvariable=self.project_coverage_variable)
        project_coverage_label.grid(row=2, column=1, sticky='we', padx=10)

        project_exec_time_label = customtkinter.CTkLabel(self.frame, textvariable=self.project_exec_time_variable)
        project_exec_time_label.grid(row=2, column=2, sticky='we', padx=10)

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)

    def on_project_change(self, target_project: TargetProject):
        if target_project.valid_project:
            self.project_path_variable.set(target_project.project_path)
            self.project_num_tests_variable.set(
                'Number of Test Cases: ' + str(target_project.initial_coverage_data.num_of_tests))
            self.project_coverage_variable.set(
                'Tests Coverage: ' + str(round(target_project.initial_coverage_data.coverage, 2)) + '%')
            self.project_exec_time_variable.set(
                'Tests Execution Time: ' + str(round(target_project.initial_coverage_data.exec_time, 2)) + 's')
        else:
            self.project_path_variable.set(value='None')
            self.project_num_tests_variable.set(value='Number of Tests: 0')
            self.project_coverage_variable.set(value='Project Coverage: 0%')
            self.project_exec_time_variable.set(value='Tests Execution Time: 0s')
