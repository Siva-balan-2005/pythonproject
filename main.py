from models.loan import Loan
from models.prepayment import Prepayment
from calculations.amortization import generate_schedule
from analysis.stats import summary, yearly_summary
from analysis.comparator import compare
from visual.charts import plot_balance, plot_interest_principal
from storage.csv_handler import save_to_csv
from utils.validators import validate


def main():
    print("==== EMI MASTER ====")

    p = float(input("Enter Principal: "))
    r = float(input("Enter Interest Rate: "))
    t = int(input("Enter Tenure (months): "))

    validate(p, r, t)

    loan = Loan(p, r, t)

    emi = loan.calculate_emi()
    print(f"\nEMI: {round(emi,2)}")

    choice = input("Do you want prepayment? (y/n): ")

    prepayments = []

    if choice == "y":
        amt = float(input("Enter prepayment amount: "))
        month = int(input("Enter month: "))
        prepayments.append(Prepayment(amt, month))

    df = generate_schedule(loan, prepayments)

    print("\nAmortization Table:")
    print(df.head())

    print("\nSummary:")
    print(summary(df))

    print("\nYearly Summary:")
    print(yearly_summary(df))

    save_to_csv(df, "schedule.csv")

    plot_balance(df)
    plot_interest_principal(df)


if __name__ == "__main__":
    main()