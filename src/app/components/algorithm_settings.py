import tkinter as tk

import customtkinter

from src.app.components.custom_component import CustomComponent
from src.app.components.frame_title import FrameTitle
from src.optimisation.configs.algorithm_config import AlgorithmConfig


class AlgorithmSettings(CustomComponent):
    def __init__(self, root: customtkinter.CTk, algorithm: tk.StringVar):
        self.frame = None
        self.algorithm = algorithm
        super().__init__(root)

    def layout_elements(self, root: customtkinter.CTk):
        self.frame = customtkinter.CTkFrame(root, bg_color='transparent', fg_color='transparent', border_color='grey',
                                            border_width=2)
        self.frame.grid_propagate(False)
        self.frame.grid_columnconfigure((0, 1), weight=1)
        self.frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        title = FrameTitle(self.frame, text='ALGORITHM SETTINGS')
        title.grid(row=0, column=0, columnspan=2)
        # label = customtkinter.CTkLabel(root, textvariable=self.algorithm)
        # label.pack()

    def get_algorithm_config(self) -> AlgorithmConfig:
        pass

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)
