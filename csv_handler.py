def save_to_csv(df, filename):
    df.to_csv(filename, index=False)


def load_csv(filename):
    import pandas as pd
    return pd.read_csv(filename)