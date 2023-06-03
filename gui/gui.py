import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import calculator


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Annuity Progression')
        self.geometry("1280x720")
        self.configure(bg='#041E42')

        # Create a frame for the labels and entries
        self.frame_inputs = ttk.Frame(self)
        self.frame_inputs.grid(row=0, column=2, pady=10,
                               padx=(0, 10), sticky="ne")

        # Create a labels and entries
        self.label_n = ttk.Label(
            self.frame_inputs, text="Number of Periods (n):")
        self.entry_n = ttk.Entry(self.frame_inputs)
        self.label_p = ttk.Label(
            self.frame_inputs, text="Principal Amount (p):")
        self.entry_p = ttk.Entry(self.frame_inputs)
        self.label_pmt = ttk.Label(
            self.frame_inputs, text="Payment Amount (pmt):")
        self.entry_pmt = ttk.Entry(self.frame_inputs)
        self.label_r = ttk.Label(self.frame_inputs, text="Interest Rate (r%):")
        self.entry_r = ttk.Entry(self.frame_inputs)

        self.label_n.grid(row=0, column=0, sticky="w")
        self.entry_n.grid(row=0, column=1)
        self.label_p.grid(row=1, column=0, sticky="w")
        self.entry_p.grid(row=1, column=1)
        self.label_pmt.grid(row=2, column=0, sticky="w")
        self.entry_pmt.grid(row=2, column=1)
        self.label_r.grid(row=3, column=0, sticky="w")
        self.entry_r.grid(row=3, column=1)

        # Create a switch to select annuity type
        self.label_switch = tk.Label(self.frame_inputs, text="Annuity Type:")
        self.switch_var = tk.StringVar()
        self.switch_var.set("Ordinary")
        self.switch_ordinary = tk.Radiobutton(
            self.frame_inputs, text="Ordinary Annuity", variable=self.switch_var, value="Ordinary")
        self.switch_due = tk.Radiobutton(
            self.frame_inputs, text="Annuity Due", variable=self.switch_var, value="Due")

        self.label_switch.grid(row=4, column=0, sticky="w")
        self.switch_ordinary.grid(row=4, column=1, sticky="w")
        self.switch_due.grid(row=5, column=1, sticky="w")

        # Create a frame for the buttons
        self.frame_buttons = ttk.Frame(self)
        self.frame_buttons.grid(row=1, column=2, pady=(
            0, 10), padx=(0, 10), sticky="ne")

        # Create a button to calculate the annuity
        self.button_calculate = tk.Button(
            self.frame_buttons, text="Calculate", command=self.calculate_annuity)
        self.button_calculate.grid(row=0, column=0, pady=10)

        # Create a button to export the table to an Excel file
        self.button_export = tk.Button(
            self.frame_buttons, text="Export to Excel", command=self.export_to_excel)
        self.button_export.grid(row=0, column=1, pady=10)

        # Create a frame for the table
        self.frame_table = ttk.Frame(self)
        self.frame_table.grid(row=2, column=0, columnspan=3,
                              pady=(0, 10), padx=10, sticky="w")

        # Create a Treeview widget to display the result as a table
        self.treeview = ttk.Treeview(self.frame_table, show="headings")
        self.treeview.pack(side="left", fill="both", expand=True)

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

        # Create a frame for the line chart
        self.frame_chart = ttk.Frame(self)
        self.frame_chart.grid(row=0, column=0, rowspan=2,
                              columnspan=2, padx=10, pady=10, sticky="nw")

        # Create line chart
        self.fig, self.ax = plt.subplots(figsize=(9, 4))
        self.ax.set_xlabel('Period')
        self.ax.set_ylabel('Value')
        self.ax.set_title('Annuity Progression')
        self.canvas = FigureCanvasTkAgg(self.fig, self.frame_chart)
        self.canvas.get_tk_widget().pack()

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

        self.ax.clear()
        self.ax.set_xlabel('Period')
        self.ax.set_ylabel('Value')
        self.ax.set_title('Annuity Progression')
        self.ax.plot(df['Period'], df['Ending_Value'],
                     label='Ending Value', color='lightblue')
        self.ax.plot(df['Period'], df['Total_Contributions'],
                     label='Total Contributions', color='darkblue')
        self.ax.fill_between(df['Period'], df['Ending_Value'], alpha=0.3)
        self.ax.fill_between(
            df['Period'], df['Total_Contributions'], alpha=0.3, color='blue')
        self.ax.legend()
        self.canvas.draw()

    def export_to_excel(self):
        # Prompt the user to select the location to save the Excel file
        file_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
        if not file_path:
            return  # User canceled the save operation

        # Save the DataFrame to an Excel file
        self.export_data.to_excel(file_path, index=False)
        print("Table exported to Excel successfully.")
