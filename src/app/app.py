import customtkinter

from src.app.components.algorithm_settings import AlgorithmSettings
from src.app.components.optimisation_settings import OptimisationSettings
from src.app.components.project_loader import ProjectLoader


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Unittest Opt')
        self.after(0, lambda: self.state('zoomed'))
        self.add_app_elements()

    def add_app_elements(self):
        ProjectLoader(root=self)
        OptimisationSettings(root=self)
        AlgorithmSettings(root=self)
