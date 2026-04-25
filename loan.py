class Loan:
    def __init__(self, principal, rate, tenure):
        self.principal = principal
        self.rate = rate / 12 / 100   # monthly rate
        self.tenure = tenure          # in months

    def calculate_emi(self):
        p = self.principal
        r = self.rate
        n = self.tenure

        emi = (p * r * (1 + r)**n) / ((1 + r)**n - 1)
        return emi