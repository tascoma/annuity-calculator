import tkinter as tk
import ttkbootstrap as ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib as mpl


class LineChart(ttk.Labelframe):
    def __init__(self, parent):
        super().__init__(parent, text='Time Series')
        plt.style.use('dark_background')
        mpl.rc('font', family='Arial')
        plt.rcParams['figure.facecolor'] = '#222222'
        plt.rcParams['axes.facecolor'] = '#2f2f2f'

        self.fig, self.ax = plt.subplots(figsize=(9, 4))
        self.ax.set_xlabel('Period')
        self.ax.set_ylabel('Value')
        self.ax.set_title('Annuity Progression')
        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.get_tk_widget().pack()

    def update_chart(self, df):
        self.ax.clear()
        self.ax.plot(df['Period'], df['Ending_Value'], label='Ending Value', color='lightblue')
        self.ax.plot(df['Period'], df['Total_Contributions'], label='Total Contributions', color='darkblue')
        self.ax.fill_between(df['Period'], df['Ending_Value'], alpha=0.3)
        self.ax.fill_between(df['Period'], df['Total_Contributions'], alpha=0.3, color='blue')
        self.ax.legend()
        self.canvas.draw()