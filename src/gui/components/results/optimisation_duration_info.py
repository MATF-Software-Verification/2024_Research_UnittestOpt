import customtkinter

from src.gui.components.custom_component import CustomComponent
from src.gui.components.frame_title import FrameTitle
from src.optimisation.optimisation_report import OptimisationReport


class OptimisationDurationInfo(CustomComponent):
    def __init__(self, root: customtkinter.CTk, optimisation_report: OptimisationReport):
        self.frame = None
        self.optimisation_report = optimisation_report
        super().__init__(root)

    def layout_elements(self, root: customtkinter.CTk):
        self.frame = customtkinter.CTkFrame(root, bg_color='transparent', fg_color='transparent', border_color='grey',
                                            border_width=1)
        self.frame.grid_propagate(False)
        self.frame.grid_columnconfigure((0, 1, 2), weight=1, uniform='column')
        self.frame.grid_rowconfigure((0, 1), weight=1, uniform='row')

        title = FrameTitle(self.frame, text='OPTIMISATION DURATION INFO', font_size=12)
        title.grid(row=0, column=0, columnspan=3)

        start_time_label = customtkinter.CTkLabel(self.frame,
                                                  text='Start Time: ' +
                                                       str(self.optimisation_report.start_time).split('.')[0])
        start_time_label.grid(row=1, column=0, sticky='we', padx=10)

        end_time_label = customtkinter.CTkLabel(self.frame,
                                                text='End Time: ' + str(self.optimisation_report.end_time).split('.')[
                                                    0])
        end_time_label.grid(row=1, column=1, sticky='we', padx=10)

        duration_time_label = customtkinter.CTkLabel(self.frame,
                                                     text='Duration: ' +
                                                          str(self.optimisation_report.duration).split('.')[0])
        duration_time_label.grid(row=1, column=2, sticky='we', padx=10)

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)
