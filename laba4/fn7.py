import numpy as np

def calculate_vector_mean(lst: list) -> float:
    arr = np.array(lst)
    return float(np.mean(arr))