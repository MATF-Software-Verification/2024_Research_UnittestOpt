import customtkinter

from src.app.components.custom_component import CustomComponent
from src.optimisation.configs.optimisation_config import OptimisationConfig
from src.optimisation.target_project import TargetProject


class OptimisationSettings(CustomComponent):
    def __init__(self, root: customtkinter.CTk):
        self.min_coverage_input = None
        self.optimisation_type = customtkinter.StringVar(value="genetic")
        self.coverage_importance = customtkinter.DoubleVar(value=1)
        self.reduction_importance = customtkinter.DoubleVar(value=0.2)
        self.efficiency_importance = customtkinter.DoubleVar(value=0.1)
        self.min_coverage = customtkinter.DoubleVar(value=0)
        super().__init__(root)

    def layout_elements(self, root: customtkinter.CTk):

        coverage_importance_slider = customtkinter.CTkSlider(root, from_=0, to=1, number_of_steps=100,
                                                             variable=self.coverage_importance)
        coverage_importance_slider.pack()

        reduction_importance_slider = customtkinter.CTkSlider(root, from_=0, to=1, number_of_steps=100,
                                                              variable=self.reduction_importance)
        reduction_importance_slider.pack()

        efficiency_importance_slider = customtkinter.CTkSlider(root, from_=0, to=1, number_of_steps=100,
                                                               variable=self.efficiency_importance)
        efficiency_importance_slider.pack()

        self.min_coverage_input = customtkinter.CTkSlider(root, from_=0, to=100,
                                                          variable=self.min_coverage)
        self.min_coverage_input.pack()

        optimisation_type_input = customtkinter.CTkOptionMenu(root,
                                                              values=['random', 'genetic', 'bayesian', 'bruteforce'],
                                                              variable=self.optimisation_type)
        optimisation_type_input.pack()

    def get_optimisation_config(self) -> OptimisationConfig:
        return OptimisationConfig(optimisation_type=self.optimisation_type.get(),
                                  coverage_importance=self.coverage_importance.get(),
                                  reduction_importance=self.reduction_importance.get(),
                                  efficiency_importance=self.efficiency_importance.get(),
                                  min_coverage=self.min_coverage.get())

    def get_optimisation_type_variable(self) -> customtkinter.StringVar:
        return self.optimisation_type

    def on_project_change(self, target_project: TargetProject):
        if target_project.valid_project:
            max_coverage = int(target_project.initial_coverage_data.coverage)
            self.min_coverage_input.configure(to=max_coverage)
            if self.min_coverage.get() > max_coverage:
                self.min_coverage.set(max_coverage)
