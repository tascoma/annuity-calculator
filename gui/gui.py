import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog
import calculator
from gui.input_widget import Input
from gui.output_widget import Output
from gui.button_widget import Buttons
from gui.line_chart_widget import LineChart
from gui.table_widget import DataTable


class App(ttk.Window):
    def __init__(self):
        super().__init__(themename="darkly")
        self.title('Annuity Progression')
        self.geometry("1280x720")
        self.columnconfigure((0,1,2), weight=1)
        self.rowconfigure((0,1,2), weight=1)

        self.frame = ttk.Frame(self)
        self.frame.grid(row=0, column=2, columnspan=2, padx=10, pady=10)

        self.inputs = Input(self.frame)
        self.inputs.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        self.outputs = Output(self.frame)
        self.outputs.grid(row=1, column=0, padx=10, pady=10, sticky="nw")

        self.buttons = Buttons(self.frame, calculate_command=self.calculate_annuity, export_command=self.export_to_excel)
        self.buttons.grid(row=3, column=0, padx=10, pady=10, sticky="sw")

        self.line_chart = LineChart(self)
        self.line_chart.grid(row=0, column=0, rowspan=2, columnspan=2, padx=10, pady=10, sticky="e")

        self.data_table = DataTable(self)
        self.data_table.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="s")


    def calculate_annuity(self):
        # Retrieve the parameter values from text entry fields
        n = int(self.inputs.entry_n.get())
        p = float(self.inputs.entry_p.get())
        pmt = float(self.inputs.entry_pmt.get())
        r = float(self.inputs.entry_r.get())

        annuity_type = self.inputs.switch_var.get()
        if annuity_type == "Ordinary":
            df = calculator.ordinary_annuity(n, p, pmt, r)
        elif annuity_type == "Due":
            df = calculator.annuity_due(n, p, pmt, r)
        else:
            return

        # Insert data into Table
        self.data_table.insert_data(df)

        # Store the DataFrame for exporting
        self.export_data = df

        # Calculate outputs
        self.total_contributions = self.outputs.calculate_total_contributions(df)
        self.total_int_earned = self.outputs.calculate_total_int_earned(df)
        self.total_value = self.outputs.calculate_total_value(df)

        # Update ouputs
        self.outputs.update_ttl_contributions(self.total_contributions)
        self.outputs.update_ttl_int_earned(self.total_int_earned)
        self.outputs.update_ttl_value(self.total_value)

        # Update chart
        self.line_chart.update_chart(df)


    def export_to_excel(self):
        # Prompt the user to select the location to save the Excel file
        file_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
        if not file_path:
            return  # User canceled the save operation

        # Save the DataFrame to an Excel file
        self.export_data.to_excel(file_path, index=False)
