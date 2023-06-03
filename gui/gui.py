import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib as mpl
import calculator


class App(ttk.Window):
    def __init__(self):
        super().__init__(themename="darkly")
        self.title('Annuity Progression')
        self.geometry("1280x720")

        # Create a frame for the line chart
        self.frame_chart = ttk.Labelframe(self, text="Time Series")
        self.frame_chart.grid(row=0, column=0, rowspan=2, columnspan=2, padx=10, pady=10, sticky="e")

        # Create a frame for inputs, output, and button frames
        self.frame = ttk.Frame(self)
        self.frame.grid(row = 0, column=2, columnspan=2, padx=10, pady=10)

        # Create a frame for the inputs
        self.frame_inputs = ttk.Labelframe(self.frame, text='Inputs')
        self.frame_inputs.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        # Create a frame for the outputs
        self.frame_outputs = ttk.Labelframe(self.frame, text='Outputs')
        self.frame_outputs.grid(row=1, column=0, padx=10, pady=10, sticky="nw")

        # Create a frame for the buttons
        self.frame_buttons = ttk.Frame(self.frame)
        self.frame_buttons.grid(row=3, column=0, padx=10, pady=10, sticky="se")

        # Create a frame for the table
        self.frame_table = ttk.Frame(self)
        self.frame_table.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="s")

        # Create input labels, entries, and radiobuttons
        self.label_n = ttk.Label(self.frame_inputs, text="Number of Periods (n):")
        self.label_p = ttk.Label(self.frame_inputs, text="Principal Amount (p):")
        self.label_pmt = ttk.Label(self.frame_inputs, text="Payment Amount (pmt):")
        self.label_r = ttk.Label(self.frame_inputs, text="Interest Rate (r%):")
        self.label_switch = ttk.Label(self.frame_inputs, text="Annuity Type:")

        self.label_n.grid(row=0, column=0, sticky="w")
        self.label_p.grid(row=1, column=0, sticky="w")
        self.label_pmt.grid(row=2, column=0, sticky="w")
        self.label_r.grid(row=3, column=0, sticky="w")
        self.label_switch.grid(row=4, column=0, sticky="w")

        self.entry_n = ttk.Entry(self.frame_inputs)
        self.entry_p = ttk.Entry(self.frame_inputs)
        self.entry_pmt = ttk.Entry(self.frame_inputs)
        self.entry_r = ttk.Entry(self.frame_inputs)

        self.entry_n.grid(row=0, column=1)
        self.entry_p.grid(row=1, column=1)
        self.entry_pmt.grid(row=2, column=1)
        self.entry_r.grid(row=3, column=1)

        self.switch_var = tk.StringVar()
        self.switch_var.set("Ordinary")
        self.switch_ordinary = ttk.Radiobutton(self.frame_inputs, text="Ordinary Annuity", variable=self.switch_var, value="Ordinary")
        self.switch_due = ttk.Radiobutton(self.frame_inputs, text="Annuity Due", variable=self.switch_var, value="Due")

        self.switch_ordinary.grid(row=4, column=1, sticky="w")
        self.switch_due.grid(row=5, column=1, sticky="w")

        # Create output labels
        self.label_ttl_contributions = ttk.Label(self.frame_outputs, text='Total Contributions:')
        self.label_ttl_int_earned = ttk.Label(self.frame_outputs, text='Total Interest Earned:')
        self.label_ttl_value = ttk.Label(self.frame_outputs, text='Total Value:')

        self.label_ttl_contributions.grid(row=0, column=0, sticky="w")
        self.label_ttl_int_earned.grid(row=1, column=0, pady=10, sticky="w")
        self.label_ttl_value.grid(row=2, column=0, sticky="w")

        self.label_ttl_contributions_value = ttk.Label(self.frame_outputs, text="Pending Inputs")
        self.label_ttl_int_earned_value = ttk.Label(self.frame_outputs, text="Pending Inputs")
        self.label_ttl_value_value = ttk.Label(self.frame_outputs, text="Pending Inputs")

        self.label_ttl_contributions_value.grid(row=0, column=1)
        self.label_ttl_int_earned_value.grid(row=1, column=1)
        self.label_ttl_value_value.grid(row=2, column=1)

        # Create a button to calculate the annuity
        self.button_calculate = ttk.Button(self.frame_buttons, text="Calculate", command=self.calculate_annuity)
        self.button_calculate.grid(row=0, column=0, pady=10)

        # Create a button to export the table to an Excel file
        self.button_export = ttk.Button(self.frame_buttons, text="Export Table to Excel", command=self.export_to_excel)
        self.button_export.grid(row=0, column=1, pady=10)

        # Create a Treeview widget to display the result as a table
        self.treeview = ttk.Treeview(self.frame_table, show="headings")
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

        # Create line chart
        plt.style.use('dark_background')
        mpl.rc('font', family='Arial')
        plt.rcParams['figure.facecolor'] = '#222222'
        plt.rcParams['axes.facecolor'] = '#2f2f2f'
        
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

        # Store output values
        self.total_contributions = df['Total_Contributions'].iloc[-1]
        self.total_int_earned = round(df['Interest_Earned'].sum(), 2)
        self.total_value = df['Ending_Value'].iloc[-1]

        self.label_ttl_contributions_value.config(text=f"{self.total_contributions}")
        self.label_ttl_int_earned_value.config(text=f"{self.total_int_earned}")
        self.label_ttl_value_value.config(text=f"{self.total_value}")

        # Creat Chart
        self.ax.clear()
        self.ax.set_xlabel('Period')
        self.ax.set_ylabel('Value')
        self.ax.set_title('Annuity Progression')
        self.ax.plot(df['Period'], df['Ending_Value'], label='Ending Value', color='lightblue')
        self.ax.plot(df['Period'], df['Total_Contributions'],label='Total Contributions', color='darkblue')
        self.ax.fill_between(df['Period'], df['Ending_Value'], alpha=0.3)
        self.ax.fill_between(df['Period'], df['Total_Contributions'], alpha=0.3, color='blue')
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
