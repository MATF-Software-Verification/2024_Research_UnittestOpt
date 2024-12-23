import tkinter as tk

import customtkinter

from src.app.components.custom_component import CustomComponent
from src.optimisation.configs.algorithm_config import AlgorithmConfig


class AlgorithmSettings(CustomComponent):
    def __init__(self, root: customtkinter.CTk, algorithm: tk.StringVar):
        self.algorithm = algorithm
        super().__init__(root)

    def layout_elements(self, root: customtkinter.CTk):
        label = customtkinter.CTkLabel(root, textvariable=self.algorithm)
        label.pack()

    def get_algorithm_config(self) -> AlgorithmConfig:
        pass
