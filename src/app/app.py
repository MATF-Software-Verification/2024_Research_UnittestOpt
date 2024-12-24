import customtkinter

from src.app.components.project.project_info import ProjectInfo
from src.app.components.project.project_loader import ProjectLoader
from src.app.components.settings.settings import Settings
from src.optimisation.optimisation import Optimisation


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.target_project = None
        self.settings = None
        self.project_loader = None
        self.project_info = None
        self.title('Unittest Opt')
        self.after(0, lambda: self.state('zoomed'))
        self.add_app_elements()
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

    def add_app_elements(self):
        left_frame = customtkinter.CTkFrame(self, bg_color='transparent', fg_color='transparent')
        left_frame.grid(column=0, row=0, sticky='nswe')
        left_frame.grid_columnconfigure(0, weight=1)
        left_frame.grid_propagate(False)
        left_frame.grid_rowconfigure((0, 1, 3), weight=1, uniform='row')
        left_frame.grid_rowconfigure(2, weight=4, uniform='row')

        self.project_loader = ProjectLoader(root=left_frame, on_project_change=self.on_project_change)
        self.project_loader.grid(column=0, row=0, sticky='nswe', padx=5, pady=5)

        self.project_info = ProjectInfo(root=left_frame)
        self.project_info.grid(column=0, row=1, sticky='nswe', padx=5, pady=5)

        self.settings = Settings(root=left_frame)
        self.settings.grid(column=0, row=2, sticky='nswe')

        self.optimisation_button = customtkinter.CTkButton(left_frame, text='Start Optimisation',
                                                           command=self.start_optimisation, state='disabled')
        self.optimisation_button.grid(row=3, column=0)

        right_frame = customtkinter.CTkFrame(self, bg_color='transparent', fg_color='transparent')
        right_frame.grid(column=1, row=0, sticky='nswe')
        right_frame.grid_propagate(False)
        right_frame.grid_columnconfigure(0, weight=1)
        right_frame.grid_rowconfigure(0, weight=1)

    def on_project_change(self):
        self.target_project = self.project_loader.get_target_project()
        self.project_info.on_project_change(self.target_project)
        self.settings.on_project_change(self.target_project)
        if self.target_project.valid_project:
            self.optimisation_button.configure(state='normal')
        else:
            self.optimisation_button.configure(state='disabled')

    def start_optimisation(self):
        optimisation = Optimisation(target_project=self.target_project,
                                    optimisation_config=self.settings.get_optimisation_config(),
                                    algorithm_config=self.settings.get_algorithm_config())
        result = optimisation.run()
        print(result)
