import customtkinter

from src.app.components.custom_component import CustomComponent
from src.app.components.settings.bayesian_settings import BayesianSettings
from src.app.components.settings.bruteforce_settings import BruteforceSettings
from src.app.components.settings.genetic_settings import GeneticSettings
from src.app.components.settings.random_settings import RandomSettings
from src.optimisation.configs.algorithm_config import AlgorithmConfig


class AlgorithmSettings(CustomComponent):
    def __init__(self, root: customtkinter.CTk, algorithm: str):
        self.bruteforce_settings = None
        self.bayesian_settings = None
        self.random_settings = None
        self.genetic_settings = None
        self.frame = None
        self.algorithm = algorithm
        super().__init__(root)

    def layout_elements(self, root: customtkinter.CTk):
        self.frame = customtkinter.CTkFrame(root, bg_color='transparent', fg_color='transparent')
        self.frame.grid_propagate(False)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)

        if self.algorithm == 'genetic':
            self.genetic_settings = GeneticSettings(self.frame)
            self.genetic_settings.grid(column=0, row=0, sticky='nswe')
        elif self.algorithm == 'random':
            self.random_settings = RandomSettings(self.frame)
            self.random_settings.grid(column=0, row=0, sticky='nswe')
        elif self.algorithm == 'bayesian':
            self.bayesian_settings = BayesianSettings(self.frame)
            self.bayesian_settings.grid(column=0, row=0, sticky='nswe')
        elif self.algorithm == 'bruteforce':
            self.bruteforce_settings = BruteforceSettings(self.frame)
            self.bruteforce_settings.grid(column=0, row=0, sticky='nswe')
        else:
            pass

    def get_algorithm_config(self) -> AlgorithmConfig:
        if self.algorithm == 'genetic':
            return self.genetic_settings.get_generic_config()
        elif self.algorithm == 'random':
            return self.random_settings.get_random_config()
        elif self.algorithm == 'bayesian':
            return self.bayesian_settings.get_bayesian_config()
        elif self.algorithm == 'bruteforce':
            return self.bruteforce_settings.get_bruteforce_config()
        else:
            raise NotImplementedError

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)
