import customtkinter

from src.app.components.custom_component import CustomComponent
from src.app.components.settings.algorithm_settings import AlgorithmSettings
from src.app.components.settings.optimisation_settings import OptimisationSettings
from src.optimisation.configs.algorithm_config import AlgorithmConfig
from src.optimisation.configs.optimisation_config import OptimisationConfig
from src.optimisation.target_project import TargetProject


class Settings(CustomComponent):
    def __init__(self, root: customtkinter.CTk):
        self.frame = None
        self.optimisation_settings = None
        self.algorithm_settings = None
        super().__init__(root)

    def layout_elements(self, root: customtkinter.CTk):
        self.frame = customtkinter.CTkFrame(root, bg_color='transparent', fg_color='transparent')
        self.frame.grid_propagate(False)
        self.frame.grid_columnconfigure((0, 1), weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.optimisation_settings = OptimisationSettings(root=self.frame)
        self.optimisation_settings.grid(column=0, row=0, sticky='nswe', padx=5, pady=5)
        self.algorithm_settings = AlgorithmSettings(root=self.frame,
                                                    algorithm=self.optimisation_settings.get_optimisation_type_variable())
        self.algorithm_settings.grid(column=1, row=0, sticky='nswe', padx=5, pady=5)

    def get_optimisation_config(self) -> OptimisationConfig:
        return self.optimisation_settings.get_optimisation_config()

    def get_algorithm_config(self) -> AlgorithmConfig:
        return self.algorithm_settings.get_algorithm_config()

    def on_project_change(self, target_project: TargetProject):
        self.optimisation_settings.on_project_change(target_project)

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)
