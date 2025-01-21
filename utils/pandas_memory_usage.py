import pandas as pd

def memory_usage_by_column(df):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("memory_usage_by_column input argument needs to be a pd.DataFrame")
    
    mem_usage = df.memory_usage(deep=True)
    mem_usage_mb = mem_usage / (1024 ** 2) # Bytes > KB > MB
    
    result = pd.DataFrame({'Column': mem_usage_mb.index, 'Memory_Usage': mem_usage_mb.values.round(2)})
    return result.reset_index(drop=True)