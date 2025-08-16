import customtkinter

from src.gui.components.custom_component import CustomComponent
from src.gui.components.frame_title import FrameTitle
from src.optimisation.optimisation_report import OptimisationReport


class OptimisationSummaryInfo(CustomComponent):
    def __init__(self, root: customtkinter.CTk, optimisation_report: OptimisationReport):
        self.frame = None
        self.optimisation_report = optimisation_report
        super().__init__(root)

    def layout_elements(self, root: customtkinter.CTk):
        self.frame = customtkinter.CTkFrame(root, bg_color='transparent', fg_color='transparent', border_color='grey',
                                            border_width=1)
        self.frame.grid_propagate(False)
        self.frame.grid_columnconfigure((0, 1, 2), weight=1, uniform='column')
        self.frame.grid_rowconfigure((0, 1, 2), weight=1, uniform='row')
        self.frame.grid_rowconfigure(3, weight=2, uniform='row')

        title = FrameTitle(self.frame, text='OPTIMISATION SUMMARY INFO', font_size=12)
        title.grid(row=0, column=0, columnspan=3)

        num_of_tests_label = customtkinter.CTkLabel(self.frame,
                                                    text='Number of Excluded Tests: ' + str(
                                                        len(self.optimisation_report.excluded_test_cases)))
        num_of_tests_label.grid(row=1, column=0, sticky='we', padx=10)

        coverage_label = customtkinter.CTkLabel(self.frame, text='Coverage Loss: ' + str(
            round(self.optimisation_report.coverage_loss, 2)) + '%')
        coverage_label.grid(row=1, column=1, sticky='we', padx=10)

        exec_time_label = customtkinter.CTkLabel(self.frame,
                                                 text='Execution Time Gain: ' + str(
                                                     round(self.optimisation_report.exec_time_gain, 2)) + 's')
        exec_time_label.grid(row=1, column=2, sticky='we', padx=10)

        text_box_title = customtkinter.CTkLabel(self.frame,
                                                text='EXCLUDED TEST CASES', text_color=("#3a7ebf", "#1f538d"))
        text_box_title.grid(row=2, column=0, columnspan=3, sticky='we', padx=10)

        text_box = customtkinter.CTkTextbox(self.frame)
        text_box.grid(row=3, column=0, columnspan=3, sticky='nswe', padx=10, pady=10)

        for idx, test_case in enumerate(self.optimisation_report.excluded_test_cases):
            text_box.insert(index=str(idx) + '.0', text=test_case + '\n')
        text_box.configure(state='disabled')

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)
