import tkinter as tk
import ttkbootstrap as ttk

class Input(ttk.Labelframe):
    def __init__(self, parent):
        super().__init__(parent, text='Inputs')
    
        self.label_n = ttk.Label(self, text="Number of Periods (n):")
        self.label_p = ttk.Label(self, text="Principal Amount (p):")
        self.label_pmt = ttk.Label(self, text="Payment Amount (pmt):")
        self.label_r = ttk.Label(self, text="Interest Rate (r%):")
        self.label_switch = ttk.Label(self, text="Annuity Type:")

        self.label_n.grid(row=0, column=0, sticky="w")
        self.label_p.grid(row=1, column=0, sticky="w")
        self.label_pmt.grid(row=2, column=0, sticky="w")
        self.label_r.grid(row=3, column=0, sticky="w")
        self.label_switch.grid(row=4, column=0, sticky="w")

        self.entry_n = ttk.Entry(self)
        self.entry_p = ttk.Entry(self)
        self.entry_pmt = ttk.Entry(self)
        self.entry_r = ttk.Entry(self)

        self.entry_n.grid(row=0, column=1)
        self.entry_p.grid(row=1, column=1)
        self.entry_pmt.grid(row=2, column=1)
        self.entry_r.grid(row=3, column=1)

        self.switch_var = tk.StringVar()
        self.switch_var.set("Ordinary")
        self.switch_ordinary = ttk.Radiobutton(self, text="Ordinary Annuity", variable=self.switch_var, value="Ordinary")
        self.switch_due = ttk.Radiobutton(self, text="Annuity Due", variable=self.switch_var, value="Due")

        self.switch_ordinary.grid(row=4, column=1, sticky="w")
        self.switch_due.grid(row=5, column=1, sticky="w")