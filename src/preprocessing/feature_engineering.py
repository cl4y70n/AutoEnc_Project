
import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_features(df):
    numeric_cols = df.select_dtypes(include=['float64','int64']).columns
    df[numeric_cols] = StandardScaler().fit_transform(df[numeric_cols])
    return df
