import matplotlib.pyplot as plt


def line_chart(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['Period'], df['Ending_Value'],
            label='Ending Value', color='lightblue')
    ax.plot(df['Period'], df['Total_Contributions'],
            label='Total Contributions', color='darkblue')
    ax.fill_between(df['Period'], df['Ending_Value'], alpha=0.3)
    ax.fill_between(df['Period'], df['Total_Contributions'],
                    alpha=0.3, color='blue')
    ax.set_xlabel('Period')
    ax.set_ylabel('Value')
    ax.set_title('Annuity Progression')
    ax.legend()
    return plt.show()
