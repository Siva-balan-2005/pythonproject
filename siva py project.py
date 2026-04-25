import math

# ---------------- VALIDATION FUNCTIONS ---------------- #

def validate_rate(rate):
    if rate <= 0:
        raise ValueError("Interest rate must be greater than 0")
    return rate


def validate_tenure(tenure):
    if tenure <= 0:
        raise ValueError("Tenure must be greater than 0")
    return tenure


# ---------------- CORE CALCULATION FUNCTIONS ---------------- #

def calculate_tenure(years):
    return years * 12


def compute_emi(principal, annual_rate, tenure_years):
    validate_rate(annual_rate)
    validate_tenure(tenure_years)

    monthly_rate = annual_rate / (12 * 100)
    months = calculate_tenure(tenure_years)

    emi = principal * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)
    return emi, months


def compute_monthly_interest(principal, annual_rate):
    monthly_rate = annual_rate / (12 * 100)
    return principal * monthly_rate


def compute_monthly_principal(emi, interest):
    return emi - interest


# ---------------- PREPAYMENT FUNCTION ---------------- #

def reduce_emi(principal, annual_rate, tenure_years, prepayment):
    if prepayment <= 0 or prepayment >= principal:
        raise ValueError("Prepayment must be between 0 and loan amount")

    new_principal = principal - prepayment
    new_emi, months = compute_emi(new_principal, annual_rate, tenure_years)

    return new_principal, new_emi, months


# ---------------- MENU SYSTEM ---------------- #

def display_menu():
    print("\n====== EMI MASTER MENU ======")
    print("1. Calculate EMI")
    print("2. First Month Breakdown")
    print("3. Prepayment Simulation")
    print("4. Exit")


# ---------------- MAIN PROGRAM ---------------- #

def main():
    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                principal = float(input("Enter loan amount: "))
                rate = float(input("Enter annual interest rate (%): "))
                tenure = int(input("Enter tenure (years): "))

                emi, months = compute_emi(principal, rate, tenure)

                print(f"\nMonthly EMI: {emi:.2f}")
                print(f"Tenure (months): {months}")

            elif choice == 2:
                principal = float(input("Enter loan amount: "))
                rate = float(input("Enter annual interest rate (%): "))
                tenure = int(input("Enter tenure (years): "))

                emi, _ = compute_emi(principal, rate, tenure)

                interest = compute_monthly_interest(principal, rate)
                principal_component = compute_monthly_principal(emi, interest)

                print("\n--- First Month Breakdown ---")
                print(f"EMI: {emi:.2f}")
                print(f"Interest Component: {interest:.2f}")
                print(f"Principal Component: {principal_component:.2f}")

            elif choice == 3:
                principal = float(input("Enter loan amount: "))
                rate = float(input("Enter annual interest rate (%): "))
                tenure = int(input("Enter tenure (years): "))
                prepayment = float(input("Enter prepayment amount: "))

                new_principal, new_emi, months = reduce_emi(principal, rate, tenure, prepayment)

                print("\n--- Prepayment Result ---")
                print(f"Remaining Principal: {new_principal:.2f}")
                print(f"New EMI: {new_emi:.2f}")
                print(f"Tenure (months): {months}")

            elif choice == 4:
                print("Exiting EMI MASTER. Goodbye!")
                break

            else:
                print("Invalid choice. Please select a valid option.")

        except ValueError as e:
            print(f"Error: {e}")

        except Exception:
            print("Invalid input. Please try again.")


# ---------------- RUN PROGRAM ---------------- #

if __name__ == "__main__":
    main()