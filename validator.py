def validate(principal, rate, tenure):
    if principal <= 0:
        raise ValueError("Principal must be positive")

    if rate <= 0 or rate > 50:
        raise ValueError("Invalid interest rate")

    if tenure <= 0:
        raise ValueError("Invalid tenure")