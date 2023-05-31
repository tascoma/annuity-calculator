import time_value_money


def main():
    ordinary_annuity_df = time_value_money.ordinary_annuity(10, 1000, 100, 7)
    annuity_due_df = time_value_money.annuity_due(10, 1000, 100, 7)
    time_value_money.line_chart(ordinary_annuity_df)
    time_value_money.line_chart(annuity_due_df)


if __name__ == "__main__":
    main()
