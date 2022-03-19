import numpy as np
from solution1 import get_input_as_arr, binary_to_decimal

def main(file_path: str):
    input_data = get_input_as_arr(file_path)
    oxygen_generator_rating = get_oxygen_generator_rating(input_data)
    co2_scrubber_rating = get_co2_scrubber_rating(input_data)
    breakpoint()
    return binary_to_decimal(oxygen_generator_rating) * binary_to_decimal(co2_scrubber_rating)

def get_oxygen_generator_rating(array: np.ndarray):
    binary = filter_recursively(array, occurrence='most', n_col_filter=0)
    return binary

def get_co2_scrubber_rating(array: np.ndarray):
    binary = filter_recursively(array, occurrence='least', n_col_filter=0)
    return binary

def filter_recursively(array: np.ndarray, occurrence: str, n_col_filter: int=0) -> list:
    mean = np.mean(array[:, n_col_filter])
    if mean < 0.5:
        if occurrence == 'most':
            mask = (array[:, n_col_filter] == 0)
        elif occurrence == 'least':
            mask = (array[:, n_col_filter] == 1)
    elif mean == 0.5:
        if occurrence == 'most': # here most selects rows with 1
            mask = (array[:, n_col_filter] == 1)
        elif occurrence == 'least': # here least selects rows with 0
            mask = (array[:, n_col_filter] == 0)
    elif mean > 0.5:
        if occurrence == 'most':
            mask = (array[:, n_col_filter] == 1)
        elif occurrence == 'least':
            mask = (array[:, n_col_filter] == 0)
    sub_array = array[mask]
    if sub_array.shape[0] > 1:
        n_col_filter += 1
        return filter_recursively(sub_array, occurrence, n_col_filter)
    else:
        return sub_array.tolist()[0] # list of single list -> extract list


if __name__ == '__main__':
    input_path = 'input1.txt'
    out = main(input_path)
    print(out)