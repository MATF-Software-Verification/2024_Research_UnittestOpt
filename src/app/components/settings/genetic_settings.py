import customtkinter

from src.app.components.custom_component import CustomComponent
from src.app.components.frame_title import FrameTitle
from src.optimisation.configs.genetic_config import GeneticConfig


class GeneticSettings(CustomComponent):
    def __init__(self, root: customtkinter.CTk):
        self.frame = None
        self.num_of_iterations = customtkinter.IntVar(value=100)
        self.population_size = customtkinter.IntVar(value=100)
        self.elitism_factor = customtkinter.DoubleVar(value=0.3)
        self.mutation_factor = customtkinter.DoubleVar(value=0.01)
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
        self.frame.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform='column')

        title = FrameTitle(self.frame, text='GENETIC OPTIMISATION SETTINGS')
        title.grid(row=0, column=0, columnspan=3)

        num_of_iterations_label = customtkinter.CTkLabel(self.frame, text='Number of Iterations: ')
        num_of_iterations_label.grid(row=1, column=0)
        num_of_iterations_value_label = customtkinter.CTkLabel(self.frame, textvariable=self.num_of_iterations)
        num_of_iterations_value_label.grid(row=1, column=1)
        num_of_iterations_slider = customtkinter.CTkSlider(self.frame, from_=0, to=500,
                                                           variable=self.num_of_iterations,
                                                           command=lambda x: self.num_of_iterations.set(int(x)))
        num_of_iterations_slider.grid(row=1, column=2, padx=25)

        population_size_label = customtkinter.CTkLabel(self.frame, text='Population Size: ')
        population_size_label.grid(row=2, column=0)
        population_size_value_label = customtkinter.CTkLabel(self.frame, textvariable=self.population_size)
        population_size_value_label.grid(row=2, column=1)
        population_size_slider = customtkinter.CTkSlider(self.frame, from_=0, to=300,
                                                         variable=self.population_size,
                                                         command=lambda x: self.population_size.set(int(x)))
        population_size_slider.grid(row=2, column=2, padx=25)

        elitism_factor_label = customtkinter.CTkLabel(self.frame, text='Elitism Factor: ')
        elitism_factor_label.grid(row=3, column=0)
        elitism_factor_value_label = customtkinter.CTkLabel(self.frame, textvariable=self.elitism_factor)
        elitism_factor_value_label.grid(row=3, column=1)
        elitism_factor_slider = customtkinter.CTkSlider(self.frame, from_=0, to=0.5,
                                                        variable=self.elitism_factor,
                                                        command=lambda x: self.elitism_factor.set(round(x, 2)))
        elitism_factor_slider.grid(row=3, column=2, padx=25)

        mutation_factor_label = customtkinter.CTkLabel(self.frame, text='Mutation Factor: ')
        mutation_factor_label.grid(row=4, column=0)
        mutation_factor_value_label = customtkinter.CTkLabel(self.frame, textvariable=self.mutation_factor)
        mutation_factor_value_label.grid(row=4, column=1)
        mutation_factor_slider = customtkinter.CTkSlider(self.frame, from_=0, to=0.1,
                                                         variable=self.mutation_factor,
                                                         command=lambda x: self.mutation_factor.set(round(x, 3)))
        mutation_factor_slider.grid(row=4, column=2, padx=25)

        random_seed_label = customtkinter.CTkLabel(self.frame, text='Random Seed: ')
        random_seed_label.grid(row=5, column=0)
        random_seed_input = customtkinter.CTkEntry(self.frame, textvariable=self.random_seed)
        random_seed_input.grid(row=5, column=2, padx=25)

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)

    def get_genetic_config(self) -> GeneticConfig:
        return GeneticConfig(population_size=self.population_size.get(),
                             num_of_iterations=self.num_of_iterations.get(),
                             elitism_factor=self.elitism_factor.get(),
                             mutation_factor=self.mutation_factor.get(),
                             seed=int(self.random_seed.get()))
