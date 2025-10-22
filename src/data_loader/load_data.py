
import pandas as pd

def load_transaction_data(file_path):
    df = pd.read_csv(file_path)
    return df
