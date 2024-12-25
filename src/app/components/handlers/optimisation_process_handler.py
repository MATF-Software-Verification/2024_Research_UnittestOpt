import threading
from typing import Callable

import customtkinter

from src.app.components.custom_component import CustomComponent
from src.app.components.frame_title import FrameTitle
from src.app.components.project.project_info import ProjectInfo
from src.app.components.project.project_loader import ProjectLoader
from src.app.components.settings.settings import Settings
from src.optimisation.optimisation import Optimisation
from src.optimisation.optimisation_report import OptimisationReport


class OptimisationProcessHandler(CustomComponent):
    def __init__(self, root: customtkinter.CTk, on_optimisation_finished: Callable):
        self.optimisation_progressbar = None
        self.optimisation_controller_frame = None
        self.frame = None
        self.optimisation_report = None
        self.optimisation_button = None
        self.target_project = None
        self.settings = None
        self.project_loader = None
        self.project_info = None
        self.on_optimisation_finished = on_optimisation_finished
        super().__init__(root)

    def layout_elements(self, root: customtkinter.CTk):
        self.frame = customtkinter.CTkFrame(root, bg_color='transparent', fg_color='transparent')
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_propagate(False)
        self.frame.grid_rowconfigure((0, 1, 3), weight=1, uniform='row')
        self.frame.grid_rowconfigure(2, weight=4, uniform='row')

        self.project_loader = ProjectLoader(root=self.frame, on_project_change=self.on_project_change)
        self.project_loader.grid(column=0, row=0, sticky='nswe', padx=5, pady=5)

        self.project_info = ProjectInfo(root=self.frame)
        self.project_info.grid(column=0, row=1, sticky='nswe', padx=5, pady=5)

        self.settings = Settings(root=self.frame)
        self.settings.grid(column=0, row=2, sticky='nswe')

        self.optimisation_controller_frame = customtkinter.CTkFrame(self.frame, bg_color='transparent',
                                                                    fg_color='transparent', border_color='grey',
                                                                    border_width=2)
        self.add_optimisation_controller(self.optimisation_controller_frame)
        self.optimisation_controller_frame.grid(column=0, row=3, sticky='nswe', padx=5, pady=5)

    def add_optimisation_controller(self, frame):

        frame.grid_propagate(False)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure((0, 1, 2), weight=1, uniform='row')

        title = FrameTitle(frame, text='OPTIMISATION CONTROLLER')
        title.grid(row=0, column=0, columnspan=2)

        self.optimisation_button = customtkinter.CTkButton(frame, text='Start Optimisation',
                                                           command=self.trigger_optimisation, state='disabled')
        self.optimisation_button.grid(row=1, column=0, padx=25)

        self.optimisation_progressbar = customtkinter.CTkProgressBar(frame, orientation="horizontal",
                                                                     mode='indeterminate')

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)

    def on_project_change(self):
        self.target_project = self.project_loader.get_target_project()
        self.project_info.on_project_change(self.target_project)
        self.settings.on_project_change(self.target_project)
        if self.target_project.valid_project:
            self.optimisation_button.configure(state='normal')
        else:
            self.optimisation_button.configure(state='disabled')

    def trigger_optimisation(self):
        self.optimisation_progressbar.grid(row=2, column=0, padx=25)
        self.optimisation_progressbar.start()
        self.optimisation_button.configure(state='disabled')
        worker = threading.Thread(target=self.run_optimisation)
        worker.start()

    def run_optimisation(self):
        optimisation = Optimisation(target_project=self.target_project,
                                    optimisation_config=self.settings.get_optimisation_config(),
                                    algorithm_config=self.settings.get_algorithm_config())
        self.optimisation_report = optimisation.run()
        self.optimisation_progressbar.stop()
        self.optimisation_progressbar.grid_forget()
        self.optimisation_button.configure(state='normal')
        self.on_optimisation_finished()

    def get_optimisation_report(self) -> OptimisationReport:
        return self.optimisation_report
