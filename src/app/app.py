import customtkinter

from src.app.components.optimisation_process_handler import OptimisationProcessHandler
from src.app.components.optimisation_results_handler import OptimisationResultsHandler


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.optimisation_process_handler = None
        self.title('Unittest Opt')
        self.after(0, lambda: self.state('zoomed'))
        self.add_app_elements()

    def add_app_elements(self):
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.optimisation_process_handler = OptimisationProcessHandler(root=self)
        self.optimisation_process_handler.grid(column=0, row=0, sticky='nswe')

        self.optimisation_results_handler = OptimisationResultsHandler(root=self)
        self.optimisation_results_handler.grid(column=1, row=0, sticky='nswe')
