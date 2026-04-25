def calculate_emi(p, r, n):
    r = r / 12 / 100
    emi = (p * r * (1 + r)**n) / ((1 + r)**n - 1)
    return emi