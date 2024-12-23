import customtkinter

from src.app.components.custom_component import CustomComponent


class FrameTitle(CustomComponent):

    def __init__(self, root: customtkinter.CTk, text: str):
        self.title = None
        self.text = text
        self.frame = root
        super().__init__(root)

    def layout_elements(self, root: customtkinter.CTk):
        font = customtkinter.CTkFont(size=15, weight='bold')
        self.title = customtkinter.CTkLabel(root, text=self.text, font=font, height=10,
                                            text_color=("#3a7ebf", "#1f538d"))

    def grid(self, **kwargs):
        self.title.grid(sticky='n', pady=10, padx=10, **kwargs)
