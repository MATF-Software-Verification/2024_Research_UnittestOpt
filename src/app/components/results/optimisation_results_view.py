from typing import Union

import customtkinter

from src.app.components.custom_component import CustomComponent
from src.app.components.frame_title import FrameTitle
from src.app.components.results.optimisation_duration_info import OptimisationDurationInfo
from src.optimisation.optimisation_report import OptimisationReport


class OptimisationResultsView(CustomComponent):
    def __init__(self, root: customtkinter.CTk, optimisation_report: Union[OptimisationReport, None]):
        self.frame = None
        self.optimisation_report = optimisation_report
        super().__init__(root)

    def layout_elements(self, root: customtkinter.CTk):
        self.frame = customtkinter.CTkFrame(root, bg_color='transparent', fg_color='transparent', border_color='grey',
                                            border_width=2)
        self.frame.grid_propagate(False)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure((0,1,2,3), weight=1, uniform='row')

        title = FrameTitle(self.frame, text='OPTIMISATION REPORT')
        title.grid(row=0, column=0)

        if self.optimisation_report:
            optimisation_info = OptimisationDurationInfo(self.frame, self.optimisation_report)
            optimisation_info.grid(row=1, column=0, sticky='nswe')
        else:
            no_optimisation_data_label = customtkinter.CTkLabel(self.frame, text='No Optimisation Results Available')
            no_optimisation_data_label.grid(row=1, column=0, columnspan='6')

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)
