import tkinter as tk

import customtkinter

from src.app.components.custom_component import CustomComponent


class ProjectLoader(CustomComponent):

    def load_project(self):
        self.project_path = tk.filedialog.askdirectory()
        self.selected_project_label.configure(text='Selected project: ' + self.project_path)

    def get_project_path(self) -> str:
        return self.project_path

    def pack_elements(self, root: customtkinter.CTk):
        select_project_button = customtkinter.CTkButton(root, text="Load Project", command=self.load_project)
        selected_project_label = customtkinter.CTkLabel(root, text='Selected project: None')
        select_project_button.pack(padx=20, pady=20)
        selected_project_label.pack()
