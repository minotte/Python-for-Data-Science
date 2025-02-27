import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    load(path: str) -> pd.DataFrame
    description:
        loads a csv and print the shape.
    Args:
        - the path of a csv
    Error:
        - if the path is wrong or the csv can be open.
    Return:
        - DataFrame
    """
    try:
        table = pd.read_csv(path)
        print(f"Loading dataset of dimensions {table.shape}")
        return table

    except Exception as e:
        print(f"Error: {e}")
