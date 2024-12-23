import customtkinter

from src.app.components.custom_component import CustomComponent
from src.optimisation.configs.genetic_config import GeneticConfig


class GeneticSettings(CustomComponent):
    def __init__(self, root: customtkinter.CTk):
        super().__init__(root)
        self.frame = None

    def layout_elements(self, root: customtkinter.CTk):
        pass

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)

    def get_genetic_config(self) -> GeneticConfig:
        pass
