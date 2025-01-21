def pandas_clean_column_names(df):
    df.columns = (
        df.columns.str.strip()
        .str.capitalize()
        .str.replace(" ", "_")
    )
    
    return df