from abc import ABC, abstractmethod

import customtkinter


class CustomComponent(ABC):
    def __init__(self, root: customtkinter.CTk):
        super().__init__()
        self.pack_elements(root)

    @abstractmethod
    def pack_elements(self, root: customtkinter.CTk):
        raise NotImplementedError