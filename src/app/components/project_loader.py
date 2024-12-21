from typing import Callable

import customtkinter

from src.app.components.custom_component import CustomComponent


class ProjectLoader(CustomComponent):

    def __init__(self, root: customtkinter.CTk, on_project_change: Callable):
        self.project_path = None
        self.on_project_change = on_project_change
        self.selected_project_variable = customtkinter.StringVar(value='Selected project: ' + str(self.project_path))
        super().__init__(root)

    def load_project(self):
        old_project_path = self.project_path
        self.project_path = customtkinter.filedialog.askdirectory()
        self.selected_project_variable.set('Selected project: ' + str(self.project_path))
        if old_project_path != self.project_path:
            self.on_project_change()

    def get_project_path(self) -> str:
        return self.project_path

    def pack_elements(self, root: customtkinter.CTk):
        select_project_button = customtkinter.CTkButton(root, text="Load Project", command=self.load_project)
        selected_project_label = customtkinter.CTkLabel(root, textvariable=self.selected_project_variable)
        select_project_button.pack(padx=20, pady=20)
        selected_project_label.pack()
