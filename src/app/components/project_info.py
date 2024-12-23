from tkinter import messagebox

import customtkinter

from src.app.components.custom_component import CustomComponent
from src.optimisation.target_project import TargetProject


class ProjectInfo(CustomComponent):

    def __init__(self, root: customtkinter.CTk):
        self.project_path = None
        self.selected_project_variable = customtkinter.StringVar(value='Selected project: ' + str(self.project_path))
        super().__init__(root)

    def get_target_project(self) -> TargetProject:
        target_project = TargetProject(self.project_path)

        if not target_project.valid_project:
            messagebox.showinfo('Invalid Project', 'No sufficient test cases detected. Please select valid project.')
        return target_project

    def pack_elements(self, root: customtkinter.CTk):
        self.frame = customtkinter.CTkFrame(root, bg_color='transparent', fg_color='blue')
        # frame.grid_columnconfigure((0,1), weight=1)
        # frame.grid(row=0, column=0, padx=25, pady=25, sticky=customtkinter.W+customtkinter.E)

        # select_project_button = customtkinter.CTkButton(frame, text="Load Project", command=self.load_project)
        # select_project_button.grid(row=0, column=0, sticky=customtkinter.W+customtkinter.E, padx=25, pady=25)
        #
        # selected_project_label = customtkinter.CTkLabel(frame, textvariable=self.selected_project_variable)
        # selected_project_label.grid(row=0, column=1, sticky=customtkinter.W+customtkinter.E, padx=25, pady=25)

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)
