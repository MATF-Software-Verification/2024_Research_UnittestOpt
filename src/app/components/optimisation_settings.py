import customtkinter

from src.app.components.custom_component import CustomComponent
from src.optimisation.configs.optimisation_config import OptimisationConfig


class OptimisationSettings(CustomComponent):
    def __init__(self, root: customtkinter.CTk):
        self.optimisation_type = customtkinter.StringVar(value="genetic")
        self.coverage_importance = customtkinter.DoubleVar(value=1)
        self.reduction_importance = customtkinter.DoubleVar(value=0.2)
        self.efficiency_importance = customtkinter.DoubleVar(value=0.1)
        super().__init__(root)

    def pack_elements(self, root: customtkinter.CTk):
        coverage_importance_slider = customtkinter.CTkSlider(root, from_=0, to=1, number_of_steps=100,
                                                             variable=self.coverage_importance)
        coverage_importance_slider.pack()

        reduction_importance_slider = customtkinter.CTkSlider(root, from_=0, to=1, number_of_steps=100,
                                                              variable=self.reduction_importance)
        reduction_importance_slider.pack()

        efficiency_importance_slider = customtkinter.CTkSlider(root, from_=0, to=1, number_of_steps=100,
                                                               variable=self.efficiency_importance)
        efficiency_importance_slider.pack()

        optimisation_type_input = customtkinter.CTkOptionMenu(root,
                                                              values=['random', 'genetic', 'bayesian', 'bruteforce'],
                                                              variable=self.optimisation_type)
        optimisation_type_input.pack()

    def get_optimisation_config(self) -> OptimisationConfig:
        return OptimisationConfig(optimisation_type=self.optimisation_type.get(),
                                  coverage_importance=self.coverage_importance.get(),
                                  reduction_importance=self.reduction_importance.get())

    def get_optimisation_type_variable(self) -> customtkinter.StringVar:
        return self.optimisation_type
