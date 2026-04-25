import pandas as pd

def generate_schedule(loan, prepayments=None):
    balance = loan.principal
    emi = loan.calculate_emi()
    r = loan.rate

    data = []

    for month in range(1, loan.tenure + 1):
        interest = balance * r
        principal = emi - interest

        # apply prepayment
        if prepayments:
            for p in prepayments:
                if p.month == month:
                    balance -= p.amount

        balance -= principal

        if balance < 0:
            balance = 0

        data.append([
            month,
            round(emi, 2),
            round(principal, 2),
            round(interest, 2),
            round(balance, 2)
        ])

        if balance == 0:
            break

    df = pd.DataFrame(data, columns=[
        "Month", "EMI", "Principal", "Interest", "Balance"
    ])

    return df