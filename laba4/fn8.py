import pandas as pd

def create_summary_dataframe() -> str:
    df = pd.DataFrame({"Name": ["Alice", "Bob"], "Score": [85, 92]})
    return df.to_string()