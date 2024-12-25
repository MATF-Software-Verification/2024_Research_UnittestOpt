from typing import Union

import customtkinter

from src.app.components.custom_component import CustomComponent
from src.app.components.results.optimisation_results_export import OptimisationResultsExport
from src.app.components.results.optimisation_results_view import OptimisationResultsView
from src.optimisation.optimisation_report import OptimisationReport


class OptimisationResultsHandler(CustomComponent):
    def __init__(self, root: customtkinter.CTk, optimisation_report: Union[OptimisationReport, None]):
        self.frame = None
        self.optimisation_report = optimisation_report
        super().__init__(root)

    def layout_elements(self, root: customtkinter.CTk):
        self.frame = customtkinter.CTkFrame(root, bg_color='transparent', fg_color='transparent')
        self.frame.grid_propagate(False)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=6, uniform='row')
        self.frame.grid_rowconfigure(1, weight=1, uniform='row')

        optimisation_results_view = OptimisationResultsView(self.frame, self.optimisation_report)
        optimisation_results_view.grid(row=0, column=0, sticky='nswe', padx=5, pady=5)

        optimisation_results_export = OptimisationResultsExport(self.frame, self.optimisation_report)
        optimisation_results_export.grid(row=1, column=0, sticky='nswe', padx=5, pady=5)

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)
