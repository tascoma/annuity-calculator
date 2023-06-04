import tkinter as tk
import ttkbootstrap as ttk

class Buttons(ttk.Frame):
    def __init__(self, parent, calculate_command, export_command):
        super().__init__(parent)
        self.button_calculate = ttk.Button(self, text="Calculate", command=calculate_command)
        self.button_export = ttk.Button(self, text="Export Table to Excel", command=export_command)

        self.button_calculate.grid(row=0, column=0, pady=10)
        self.button_export.grid(row=0, column=1, padx=10, pady=10)