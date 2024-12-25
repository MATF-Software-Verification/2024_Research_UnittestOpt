import customtkinter

from src.app.components.custom_component import CustomComponent


class OptimisationResultsHandler(CustomComponent):
    def __init__(self, root: customtkinter.CTk):
        self.frame = None
        super().__init__(root)

    def layout_elements(self, root: customtkinter.CTk):
        self.frame = customtkinter.CTkFrame(root, bg_color='transparent', fg_color='transparent')
        self.frame.grid_propagate(False)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)
