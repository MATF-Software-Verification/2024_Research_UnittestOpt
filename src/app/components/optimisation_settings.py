import customtkinter

from src.app.components.custom_component import CustomComponent
from src.optimisation.configs.optimisation_config import OptimisationConfig


class OptimisationSettings(CustomComponent):
    def pack_elements(self, root: customtkinter.CTk):
        pass

    def get_optimisation_config(self) -> OptimisationConfig:
        pass
