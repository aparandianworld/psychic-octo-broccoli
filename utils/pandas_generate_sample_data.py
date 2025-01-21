import pandas as pd

def generate_sample_data(rows = 10):
    data = {
        "Name": [f"Person {i}" for i in range(rows)],
        "Age": [10 + i for i in range(rows)],
        "City": [f"City {i}" for i in range(rows)],
        "Salary": [1000 + i for i in range(rows)],
    }
    
    return pd.DataFrame(data)