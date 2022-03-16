def main():
    # Load input data
    with open('input1.txt', 'r') as file:
        input_data = [int(string.strip('\n')) for string in file.readlines()]
    
    # 0 -> measurement[i] <= measurement[i-1]
    # 1 -> measurement[i] > measurement[i-1]
    input_data.insert(input_data[0] + 1, 0) # insert an extra element into beginning of list guaranteed to be higher than next
    larger_than_prev = [1 if input_data[i] > input_data[i - 1] else 0 for i in range(1, len(input_data))]
    return sum(larger_than_prev)

if __name__ == '__main__':
    out = main()
    print(out)