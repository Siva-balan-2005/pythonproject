import matplotlib.pyplot as plt

def plot_balance(df):
    plt.plot(df["Month"], df["Balance"])
    plt.title("Outstanding Balance")
    plt.xlabel("Month")
    plt.ylabel("Balance")
    plt.show()


def plot_interest_principal(df):
    plt.bar(df["Month"], df["Interest"], label="Interest")
    plt.bar(df["Month"], df["Principal"], bottom=df["Interest"], label="Principal")
    plt.legend()
    plt.title("Interest vs Principal")
    plt.show()