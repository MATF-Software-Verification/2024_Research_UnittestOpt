from tkinter import messagebox

import customtkinter

from src.app.components.project_loader import ProjectLoader
from src.app.components.settings import Settings
from src.optimisation.optimisation import Optimisation
from src.optimisation.target_project import TargetProject


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.target_project = None
        self.settings = None
        self.algorithm_settings = None
        self.optimisation_settings = None
        self.project_loader = None
        self.title('Unittest Opt')
        self.after(0, lambda: self.state('zoomed'))
        self.add_app_elements()

    def add_app_elements(self):
        self.project_loader = ProjectLoader(root=self, on_project_change=self.on_project_change)
        self.settings = Settings(root=self)
        optimisation_button = customtkinter.CTkButton(self, text='Start Optimisation', command=self.start_optimisation)
        optimisation_button.pack()

    def on_project_change(self):
        self.target_project = TargetProject(self.project_loader.get_project_path())
        print(self.target_project.project_path)
        if not self.target_project.valid_project:
            messagebox.showinfo('Invalid Project', 'No sufficient test cases detected. Please select valid project.')

    def start_optimisation(self):
        optimisation = Optimisation(target_project=self.target_project,
                                    optimisation_config=self.settings.get_optimisation_config(),
                                    algorithm_config=self.algorithm_settings)
