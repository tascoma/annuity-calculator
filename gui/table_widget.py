import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *

class DataTable(ttk.Labelframe):
    def __init__(self, parent):
        super().__init__(parent, text='Data Table')

        self.coldata = [
            {"text": "Period", "stretch": False},
            {"text": "Beginning Value", "stretch": False},
            {"text": "Interest Earned", "stretch": False},
            {"text": "Payment", "stretch": False},
            {"text": "Ending Value", "stretch": False},
            {"text": "Total Contributions", "stretch": False}
        ]

        self.rowdata = []

        self.tableview = Tableview(self, coldata = self.coldata, rowdata=self.rowdata, bootstyle=PRIMARY)
        self.tableview.pack(side="left", fill="both", expand=True)

    def insert_data(self, df):
        self.tableview.delete_rows()
        for row in df.itertuples(index=False):
            self.tableview.insert_row("end", values=row)
        self.tableview.load_table_data()