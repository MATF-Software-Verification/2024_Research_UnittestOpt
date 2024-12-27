import threading
from typing import Union

import customtkinter

from src.app.components.custom_component import CustomComponent
from src.app.components.frame_title import FrameTitle
from src.optimisation.optimisation_report import OptimisationReport


class OptimisationResultsExport(CustomComponent):
    def __init__(self, root: customtkinter.CTk, optimisation_report: Union[OptimisationReport, None]):
        self.export_button = None
        self.export_progressbar = None
        self.frame = None
        self.optimisation_report = optimisation_report
        super().__init__(root)

    def layout_elements(self, root: customtkinter.CTk):
        self.frame = customtkinter.CTkFrame(root, bg_color='transparent', fg_color='transparent', border_color='grey',
                                            border_width=2)
        self.frame.grid_propagate(False)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure((0, 1, 2), weight=1, uniform='row')

        title = FrameTitle(self.frame, text='EXPORT OPTIMISATION REPORT')
        title.grid(row=0, column=0, columnspan=3)

        self.export_button = customtkinter.CTkButton(self.frame, text='Export',
                                                     command=self.trigger_export,
                                                     state='normal' if self.optimisation_report else 'disabled')
        self.export_button.grid(row=1, column=0, padx=25)

        self.export_progressbar = customtkinter.CTkProgressBar(self.frame, orientation="horizontal",
                                                               mode='indeterminate')

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)

    def trigger_export(self):
        self.export_progressbar.grid(row=2, column=0, padx=25)
        self.export_progressbar.start()
        self.export_button.configure(state='disabled')
        path = customtkinter.filedialog.askdirectory()
        worker = threading.Thread(target=self.export_report, args=[path])
        worker.start()

    def export_report(self, path):
        self.optimisation_report.export(path)
        self.export_progressbar.stop()
        self.export_progressbar.grid_forget()
        self.export_button.configure(state='normal')
