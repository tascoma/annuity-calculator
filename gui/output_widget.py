import tkinter as tk
import ttkbootstrap as ttk
import pandas as pd

class Output(ttk.Labelframe):
    def __init__(self, parent):
        super().__init__(parent, text='Outputs')
        self.label_ttl_contributions = ttk.Label(self, text='Total Contributions:')
        self.label_ttl_int_earned = ttk.Label(self, text='Total Interest Earned:')
        self.label_ttl_value = ttk.Label(self, text='Total Value:')

        self.label_ttl_contributions.grid(row=0, column=0, sticky="w")
        self.label_ttl_int_earned.grid(row=1, column=0, pady=10, sticky="w")
        self.label_ttl_value.grid(row=2, column=0, sticky="w")

        self.label_ttl_contributions_value = ttk.Label(self, text="Pending Inputs")
        self.label_ttl_int_earned_value = ttk.Label(self, text="Pending Inputs")
        self.label_ttl_value_value = ttk.Label(self, text="Pending Inputs")

        self.label_ttl_contributions_value.grid(row=0, column=1)
        self.label_ttl_int_earned_value.grid(row=1, column=1)
        self.label_ttl_value_value.grid(row=2, column=1)

    def calculate_total_contributions(self, df):
        return df['Total_Contributions'].iloc[-1]

    def calculate_total_int_earned(self, df):
        return round(df['Interest_Earned'].sum(), 2)

    def calculate_total_value(self, df):
        return df['Ending_Value'].iloc[-1]

    def update_ttl_contributions(self, total_contributions):
        self.label_ttl_contributions_value.config(text=f"{total_contributions}")
    
    def update_ttl_int_earned(self, total_int_earned):
        self.label_ttl_int_earned_value.config(text=f"{total_int_earned}")
    
    def update_ttl_value(self, total_value):
        self.label_ttl_value_value.config(text=f"{total_value}")