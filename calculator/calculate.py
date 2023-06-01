import pandas as pd


def ordinary_annuity(n, p, pmt, r):
    df = []
    contributions = p
    beg_val = p
    for i in range(n):
        row = []
        i += 1
        row.append(i)
        row.append(beg_val)
        interest_earned = round((r/100) * beg_val, 2)
        row.append(interest_earned)
        row.append(pmt)
        end_val = beg_val + interest_earned + pmt
        row.append(end_val)
        contributions = contributions + pmt
        row.append(contributions)
        beg_val = end_val
        df.append(row)
    return pd.DataFrame(df, columns=['Period', 'Beginning_Value', 'Interest_Earned', 'Payment', 'Ending_Value', 'Total_Contributions'])


def annuity_due(n, p, pmt, r):
    df = []
    contributions = p
    beg_val = p
    for i in range(n):
        row = []
        i += 1
        row.append(i)
        row.append(beg_val)
        row.append(pmt)
        interest_earned = round((r/100) * (beg_val + pmt), 2)
        row.append(interest_earned)
        end_val = beg_val + interest_earned + pmt
        row.append(end_val)
        contributions = contributions + pmt
        row.append(contributions)
        beg_val = end_val
        df.append(row)
    return pd.DataFrame(df, columns=['Period', 'Beginning_Value',  'Payment', 'Interest_Earned', 'Ending_Value', 'Total_Contributions'])
