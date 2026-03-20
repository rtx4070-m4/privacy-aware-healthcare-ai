
import pandas as pd

def anonymize_data(df):
    df = df.copy()
    if "patient_id" in df.columns:
        df.drop(columns=["patient_id"], inplace=True)
    return df
