import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import calculator


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Annuity Progression')
        self.geometry("1280x720")
        self.configure(bg='#041E42')

        self.label_n = tk.Label(self, text="Number of Periods (n):")
        self.entry_n = tk.Entry(self)
        self.label_p = tk.Label(self, text="Principal Amount (p):")
        self.entry_p = tk.Entry(self)
        self.label_pmt = tk.Label(self, text="Payment Amount (pmt):")
        self.entry_pmt = tk.Entry(self)
        self.label_r = tk.Label(self, text="Interest Rate (r):")
        self.entry_r = tk.Entry(self)

        self.label_n.grid(row=0, column=0, sticky="w")
        self.entry_n.grid(row=0, column=1)
        self.label_p.grid(row=1, column=0, sticky="w")
        self.entry_p.grid(row=1, column=1)
        self.label_pmt.grid(row=2, column=0, sticky="w")
        self.entry_pmt.grid(row=2, column=1)
        self.label_r.grid(row=3, column=0, sticky="w")
        self.entry_r.grid(row=3, column=1)

        # Create a switch to select annuity type
        self.label_switch = tk.Label(self, text="Annuity Type:")
        self.switch_var = tk.StringVar()
        self.switch_var.set("Ordinary")
        self.switch_ordinary = tk.Radiobutton(
            self, text="Ordinary Annuity", variable=self.switch_var, value="Ordinary")
        self.switch_due = tk.Radiobutton(
            self, text="Annuity Due", variable=self.switch_var, value="Due")

        self.label_switch.grid(row=4, column=0, sticky="w")
        self.switch_ordinary.grid(row=4, column=1, sticky="w")
        self.switch_due.grid(row=5, column=1, sticky="w")

        # Create a button to calculate the ordinary annuity
        self.button_calculate = tk.Button(
            self, text="Calculate", command=self.calculate_annuity)
        self.button_calculate.grid(row=6, column=0, columnspan=2, pady=10)

        # Create a button to export the table to an Excel file
        self.button_export = tk.Button(
            self, text="Export to Excel", command=self.export_to_excel)
        self.button_export.grid(row=8, column=0, columnspan=2, pady=10)

        # Create a Treeview widget to display the result as a table
        self.treeview = ttk.Treeview(self, show="headings")
        self.treeview.grid(row=7, column=0, columnspan=2,
                           padx=10, pady=(20, 0), sticky="nsew")

        # Define columns for the Treeview
        self.treeview["columns"] = (
            "Period", "Beginning Value", "Interest Earned", "Payment", "Ending Value", "Total Contributions")
        self.treeview["show"] = "headings"

        # Define column headings
        self.treeview.heading("Period", text="Period")
        self.treeview.heading("Beginning Value", text="Beginning Value")
        self.treeview.heading("Interest Earned", text="Interest Earned")
        self.treeview.heading("Payment", text="Payment")
        self.treeview.heading("Ending Value", text="Ending Value")
        self.treeview.heading("Total Contributions",
                              text="Total Contributions")

    def calculate_annuity(self):
        # Retrieve the parameter values from text entry fields
        n = int(self.entry_n.get())
        p = float(self.entry_p.get())
        pmt = float(self.entry_pmt.get())
        r = float(self.entry_r.get())

        annuity_type = self.switch_var.get()
        if annuity_type == "Ordinary":
            df = calculator.ordinary_annuity(n, p, pmt, r)
        elif annuity_type == "Due":
            df = calculator.annuity_due(n, p, pmt, r)
        else:
            return

        # Clear previous table data
        self.treeview.delete(*self.treeview.get_children())

        # Insert new data into the table
        for row in df.itertuples(index=False):
            self.treeview.insert("", "end", values=row)

        # Store the DataFrame for exporting
        self.export_data = df

    def export_to_excel(self):
        # Prompt the user to select the location to save the Excel file
        file_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
        if not file_path:
            return  # User canceled the save operation

        # Save the DataFrame to an Excel file
        self.export_data.to_excel(file_path, index=False)
        print("Table exported to Excel successfully.")
