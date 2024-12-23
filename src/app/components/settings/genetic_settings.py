import customtkinter

from src.app.components.custom_component import CustomComponent
from src.app.components.frame_title import FrameTitle
from src.optimisation.configs.genetic_config import GeneticConfig


class GeneticSettings(CustomComponent):
    def __init__(self, root: customtkinter.CTk):
        self.frame = None
        super().__init__(root)

    def layout_elements(self, root: customtkinter.CTk):
        self.frame = customtkinter.CTkFrame(root, bg_color='transparent', fg_color='transparent', border_color='grey',
                                            border_width=2)
        self.frame.grid_propagate(False)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)

        title = FrameTitle(self.frame, text='GENETIC OPTIMISATION SETTINGS')
        title.grid(row=0, column=0)

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)

    def get_genetic_config(self) -> GeneticConfig:
        pass
