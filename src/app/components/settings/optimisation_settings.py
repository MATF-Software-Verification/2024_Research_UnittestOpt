from typing import Callable

import customtkinter

from src.app.components.custom_component import CustomComponent
from src.app.components.frame_title import FrameTitle
from src.optimisation.configs.optimisation_config import OptimisationConfig
from src.project.target_project import TargetProject


class OptimisationSettings(CustomComponent):
    def __init__(self, root: customtkinter.CTk, on_algorithm_change: Callable):
        self.frame = None
        self.min_coverage_slider = None
        self.optimisation_type = customtkinter.StringVar(value="genetic")
        self.coverage_importance = customtkinter.DoubleVar(value=1)
        self.reduction_importance = customtkinter.DoubleVar(value=0.2)
        self.efficiency_importance = customtkinter.DoubleVar(value=0.1)
        self.min_coverage = customtkinter.DoubleVar(value=0)
        self.on_algorithm_change = on_algorithm_change
        super().__init__(root)

    def layout_elements(self, root: customtkinter.CTk):

        self.frame = customtkinter.CTkFrame(root, bg_color='transparent', fg_color='transparent', border_color='grey',
                                            border_width=2)
        self.frame.grid_propagate(False)
        self.frame.grid_columnconfigure((0, 2), weight=4, uniform='column')
        self.frame.grid_columnconfigure(1, weight=1, uniform='column')
        self.frame.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        title = FrameTitle(self.frame, text='OPTIMISATION SETTINGS')
        title.grid(row=0, column=0, columnspan=3)

        coverage_importance_label = customtkinter.CTkLabel(self.frame, text='Coverage Importance: ')
        coverage_importance_label.grid(row=1, column=0)
        coverage_importance_value_label = customtkinter.CTkLabel(self.frame, textvariable=self.coverage_importance)
        coverage_importance_value_label.grid(row=1, column=1)
        coverage_importance_slider = customtkinter.CTkSlider(self.frame, from_=0, to=1,
                                                             variable=self.coverage_importance,
                                                             command=lambda x: self.coverage_importance.set(
                                                                 round(float(x), 2)))
        coverage_importance_slider.grid(row=1, column=2, padx=25)

        reduction_importance_label = customtkinter.CTkLabel(self.frame, text='Reduction Importance: ')
        reduction_importance_label.grid(row=2, column=0)
        reduction_importance_value_label = customtkinter.CTkLabel(self.frame, textvariable=self.reduction_importance)
        reduction_importance_value_label.grid(row=2, column=1)
        reduction_importance_slider = customtkinter.CTkSlider(self.frame, from_=0, to=1,
                                                              variable=self.reduction_importance,
                                                              command=lambda x: self.reduction_importance.set(
                                                                  round(float(x), 2)))
        reduction_importance_slider.grid(row=2, column=2, padx=25)

        efficiency_importance_label = customtkinter.CTkLabel(self.frame, text='Efficiency Importance: ')
        efficiency_importance_label.grid(row=3, column=0)
        efficiency_importance_value_label = customtkinter.CTkLabel(self.frame, textvariable=self.efficiency_importance)
        efficiency_importance_value_label.grid(row=3, column=1)
        efficiency_importance_slider = customtkinter.CTkSlider(self.frame, from_=0, to=1,
                                                               variable=self.efficiency_importance,
                                                               command=lambda x: self.efficiency_importance.set(
                                                                   round(float(x), 2)))
        efficiency_importance_slider.grid(row=3, column=2, padx=25)

        min_coverage_label = customtkinter.CTkLabel(self.frame, text='Minimum Coverage: ')
        min_coverage_label.grid(row=4, column=0)
        min_coverage_value_label = customtkinter.CTkLabel(self.frame, textvariable=self.min_coverage)
        min_coverage_value_label.grid(row=4, column=1)
        self.min_coverage_slider = customtkinter.CTkSlider(self.frame, from_=0, to=1, variable=self.min_coverage,
                                                           command=lambda x: self.min_coverage.set(round(float(x), 2)))
        self.min_coverage_slider.grid(row=4, column=2, padx=25)

        optimisation_label = customtkinter.CTkLabel(self.frame, text='Optimisation Algorithm: ')
        optimisation_label.grid(row=5, column=0)

        optimisation_type_input = customtkinter.CTkOptionMenu(self.frame,
                                                              values=['genetic', 'bayesian', 'random', 'bruteforce'],
                                                              variable=self.optimisation_type,
                                                              command=lambda val: self.on_algorithm_change(str(val)))
        optimisation_type_input.grid(row=5, column=2, padx=25)

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
            self.min_coverage_slider.configure(to=max_coverage)
        else:
            self.min_coverage_slider.configure(to=100)
        self.min_coverage.set(0)

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)
