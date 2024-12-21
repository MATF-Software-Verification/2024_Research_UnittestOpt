import customtkinter

from src.app.components.algorithm_settings import AlgorithmSettings
from src.app.components.custom_component import CustomComponent
from src.app.components.optimisation_settings import OptimisationSettings
from src.optimisation.configs.algorithm_config import AlgorithmConfig
from src.optimisation.configs.optimisation_config import OptimisationConfig


class Settings(CustomComponent):
    def __init__(self, root: customtkinter.CTk):
        self.optimisation_settings = None
        self.algorithm_settings = None
        super().__init__(root)

    def pack_elements(self, root: customtkinter.CTk):
        self.optimisation_settings = OptimisationSettings(root=root)
        self.algorithm_settings = AlgorithmSettings(root=root,
                                                    algorithm=self.optimisation_settings.get_optimisation_type_variable())

    def get_optimisation_config(self) -> OptimisationConfig:
        return self.optimisation_settings.get_optimisation_config()

    def get_algorithm_config(self) -> AlgorithmConfig:
        return self.algorithm_settings.get_algorithm_config()
