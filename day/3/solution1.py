import numpy as np

def main(file_path: str):
    input_data = get_input_as_arr(file_path)

    proportion_of_ones = input_data.sum(axis=0)/input_data.shape[0]
    gamma_bits = [int(round(decimal)) for decimal in proportion_of_ones]
    epsilon_bits = [0 if bit else 1 for bit in gamma_bits]
    gamma_rate = binary_to_decimal(gamma_bits)
    epsilon_rate = binary_to_decimal(epsilon_bits)
    return gamma_rate * epsilon_rate

def get_input_as_arr(file_path: str):
    with open(file_path) as file:
        # Load txt-file as list of lists containing each individual bit as elements
        input_data = [list(bit_str.strip('\n')) for bit_str in file.readlines()]
    bit_grid = np.array(input_data, dtype='u1') # unsigned 8-bit int
    return bit_grid

def binary_to_decimal(binary_list: list):
    position = 0
    decimal = 0
    for bit in reversed(binary_list):
        decimal += bit * 2 ** position
        position += 1
    return decimal


if __name__ == '__main__':
    file_path = 'input1.txt'
    out = main(file_path)
    print(out)