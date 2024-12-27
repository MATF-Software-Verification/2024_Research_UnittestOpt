import customtkinter

from src.app.components.custom_component import CustomComponent
from src.app.components.frame_title import FrameTitle
from src.optimisation.configs.bayesian_config import BayesianConfig


class BayesianSettings(CustomComponent):
    def __init__(self, root: customtkinter.CTk):
        self.frame = None
        self.num_of_iterations = customtkinter.IntVar(value=100)
        self.random_seed = customtkinter.StringVar(value=42)
        self.random_seed.trace('w',
                               lambda *args: self.random_seed.set(''.join(filter(str.isdigit, self.random_seed.get()))))
        super().__init__(root)

    def layout_elements(self, root: customtkinter.CTk):
        self.frame = customtkinter.CTkFrame(root, bg_color='transparent', fg_color='transparent', border_color='grey',
                                            border_width=2)
        self.frame.grid_propagate(False)
        self.frame.grid_columnconfigure((0, 2), weight=4, uniform='column')
        self.frame.grid_columnconfigure(1, weight=1, uniform='column')
        self.frame.grid_rowconfigure((0, 1, 2), weight=1, uniform='row')

        title = FrameTitle(self.frame, text='BAYESIAN OPTIMISATION SETTINGS')
        title.grid(row=0, column=0, columnspan=3)

        num_of_iterations_label = customtkinter.CTkLabel(self.frame, text='Number of Trials: ')
        num_of_iterations_label.grid(row=1, column=0)
        num_of_iterations_value_label = customtkinter.CTkLabel(self.frame, textvariable=self.num_of_iterations)
        num_of_iterations_value_label.grid(row=1, column=1)
        num_of_iterations_slider = customtkinter.CTkSlider(self.frame, from_=10, to=500,
                                                           variable=self.num_of_iterations,
                                                           command=lambda x: self.num_of_iterations.set(int(x)))
        num_of_iterations_slider.grid(row=1, column=2, padx=25)

        random_seed_label = customtkinter.CTkLabel(self.frame, text='Random Seed: ')
        random_seed_label.grid(row=2, column=0)
        random_seed_input = customtkinter.CTkEntry(self.frame, textvariable=self.random_seed)
        random_seed_input.grid(row=2, column=2, padx=25)

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)

    def get_bayesian_config(self) -> BayesianConfig:
        return BayesianConfig(seed=int(self.random_seed.get()),
                              num_of_trials=self.num_of_iterations.get())
