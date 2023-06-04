import tkinter as tk
import ttkbootstrap as ttk

class DataTable(ttk.Labelframe):
    def __init__(self, parent):
        super().__init__(parent, text='Data Table')
        self.treeview = ttk.Treeview(self, show="headings")
        self.treeview.pack(side="left", fill="both", expand=True)

        # Define columns for the Treeview
        self.treeview["columns"] = ("Period", "Beginning Value", "Interest Earned", "Payment", "Ending Value", "Total Contributions")
        self.treeview["show"] = "headings"

        # Define column headings
        self.treeview.heading("Period", text="Period")
        self.treeview.heading("Beginning Value", text="Beginning Value")
        self.treeview.heading("Interest Earned", text="Interest Earned")
        self.treeview.heading("Payment", text="Payment")
        self.treeview.heading("Ending Value", text="Ending Value")
        self.treeview.heading("Total Contributions",text="Total Contributions")

    def insert_data(self, df):
        self.treeview.delete(*self.treeview.get_children())
        for row in df.itertuples(index=False):
            self.treeview.insert("", "end", values=row)