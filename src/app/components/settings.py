import customtkinter

from src.app.components.custom_component import CustomComponent
from src.optimisation.configs.algorithm_config import AlgorithmConfig
from src.optimisation.configs.optimisation_config import OptimisationConfig
from src.optimisation.target_project import TargetProject


class Settings(CustomComponent):
    def __init__(self, root: customtkinter.CTk):
        self.optimisation_settings = None
        self.algorithm_settings = None
        super().__init__(root)

    def layout_elements(self, root: customtkinter.CTk):
        self.frame = customtkinter.CTkFrame(root, bg_color='transparent', fg_color='green')
        # optimisation_settings_frame = customtkinter.CTkFrame(frame)
        # optimisation_settings_frame.grid(row=0, column=0)
        # algorithm_settings_frame = customtkinter.CTkFrame(frame)
        # algorithm_settings_frame.grid(row=0, column=0)
        # self.optimisation_settings = OptimisationSettings(root=optimisation_settings_frame)
        # self.algorithm_settings = AlgorithmSettings(root=algorithm_settings_frame,
        #                                             algorithm=self.optimisation_settings.get_optimisation_type_variable())

    def get_optimisation_config(self) -> OptimisationConfig:
        return self.optimisation_settings.get_optimisation_config()

    def get_algorithm_config(self) -> AlgorithmConfig:
        return self.algorithm_settings.get_algorithm_config()

    def on_project_change(self, target_project: TargetProject):
        pass
        # self.optimisation_settings.on_project_change(target_project)

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)
