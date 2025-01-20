import pandas as pd

def pandas_summary(df):
    summary = pd.DataFrame({
        "Data_Type": df.dtypes,
        "Missing_Values": df.isnull().sum(),
        "Unique_Values": df.nunique(),
        "First_Value": df.iloc[0],
        "Last_Value": df.iloc[-1],
    })
    
    return summary