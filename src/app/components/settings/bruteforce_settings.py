import customtkinter

from src.app.components.custom_component import CustomComponent


class BruteforceSettings(CustomComponent):
    def __init__(self, root: customtkinter.CTk):
        super().__init__(root)
        self.frame = None

    def layout_elements(self, root: customtkinter.CTk):
        pass

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)

    def get_bruteforce_config(self) -> None:
        return None
