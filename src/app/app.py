import customtkinter

from src.app.components.handlers.optimisation_process_handler import OptimisationProcessHandler
from src.app.components.handlers.optimisation_results_handler import OptimisationResultsHandler


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.optimisation_results_handler = None
        self.optimisation_process_handler = None
        self.optimisation_report = None
        self.title('Unittest Opt')
        self.after(0, lambda: self.state('zoomed'))
        self.add_app_elements()

    def add_app_elements(self):
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.optimisation_process_handler = OptimisationProcessHandler(root=self,
                                                                       on_optimisation_finished=self.on_optimisation_finished,
                                                                       on_project_change=self.on_project_change)
        self.optimisation_process_handler.grid(column=0, row=0, sticky='nswe')

        self.optimisation_results_handler = OptimisationResultsHandler(root=self,
                                                                       optimisation_report=self.optimisation_report)
        self.optimisation_results_handler.grid(column=1, row=0, sticky='nswe')

    def on_project_change(self):
        self.optimisation_report = None
        self.optimisation_results_handler = OptimisationResultsHandler(root=self,
                                                                       optimisation_report=self.optimisation_report)
        self.optimisation_results_handler.grid(column=1, row=0, sticky='nswe')

    def on_optimisation_finished(self):
        self.optimisation_report = self.optimisation_process_handler.get_optimisation_report()
        self.optimisation_results_handler = OptimisationResultsHandler(root=self,
                                                                       optimisation_report=self.optimisation_report)
        self.optimisation_results_handler.grid(column=1, row=0, sticky='nswe')
