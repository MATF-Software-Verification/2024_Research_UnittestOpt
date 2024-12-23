import threading
from tkinter import messagebox
from typing import Callable

import customtkinter

from src.app.components.custom_component import CustomComponent
from src.optimisation.target_project import TargetProject


class ProjectLoader(CustomComponent):

    def __init__(self, root: customtkinter.CTk, on_project_change: Callable):
        self.loading_label = None
        self.loading_progressbar = None
        self.frame = None
        self.project_path = None
        self.target_project = None
        self.on_project_change = on_project_change
        self.selected_project_variable = customtkinter.StringVar(value='Selected project: None')
        super().__init__(root)

    def select_project(self):
        self.target_project = None
        self.project_path = customtkinter.filedialog.askdirectory()
        self.selected_project_variable.set('Selected Project: ' + self.project_path.split('/')[-1])

        self.loading_label.grid_forget()
        self.loading_progressbar.grid(row=1, column=2, sticky='we', padx=25)
        self.loading_progressbar.start()
        worker = threading.Thread(target=self.load_project)
        worker.start()

    def load_project(self):
        self.target_project = TargetProject(self.project_path)
        self.on_project_change()
        self.loading_progressbar.stop()
        self.loading_progressbar.grid_forget()
        self.loading_label.grid(row=1, column=2, sticky='we', padx=25)
        if not self.target_project.valid_project:
            self.project_path = None
            self.selected_project_variable.set(value='Selected Project: None')
            self.loading_label.configure(text='No Project Loaded')
            messagebox.showinfo('Invalid Project', 'No sufficient test cases detected. Please select valid project.')
        else:
            self.loading_label.configure(text='Project Loaded')

    def get_target_project(self) -> TargetProject:
        return self.target_project

    def layout_elements(self, root: customtkinter.CTk):
        self.frame = customtkinter.CTkFrame(root, bg_color='transparent', fg_color='transparent', border_color='grey',
                                            border_width=2)
        self.frame.grid_propagate(False)
        self.frame.grid_columnconfigure((0, 1, 2), weight=1, uniform='column')
        self.frame.grid_rowconfigure((0,1), weight=1)

        title = customtkinter.CTkLabel(self.frame, text='PROJECT LOADER')
        title.grid(row=0, column=0, columnspan=3, sticky='we', padx=10)

        select_project_button = customtkinter.CTkButton(self.frame, text="Load Project", command=self.select_project)
        select_project_button.grid(row=1, column=0, padx=25)

        selected_project_label = customtkinter.CTkLabel(self.frame, textvariable=self.selected_project_variable)
        selected_project_label.grid(row=1, column=1, sticky='we', padx=25)

        self.loading_progressbar = customtkinter.CTkProgressBar(self.frame, orientation="horizontal",
                                                                mode='indeterminate')
        self.loading_label = customtkinter.CTkLabel(self.frame, text='No Project Loaded')
        self.loading_label.grid(row=1, column=2, sticky='we', padx=25)

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)
