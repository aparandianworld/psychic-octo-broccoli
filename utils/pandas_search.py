import re
import pandas as pd

def pandas_search(keyword):
    found = []
    
    if not keyword.strip():
        return []
    found = [ func for func in dir(pd) if not func.startswith('_') and keyword.lower() in func.lower() ]
    return found