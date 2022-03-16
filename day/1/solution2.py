def main():
    with open('input1.txt', 'r') as file:
        input_data = [int(string.strip("\n")) for string in file.readlines()]
    
    # list of sums of three-element windows
    three_sum = [
        sum([input_data[i - 2], input_data[i - 1], input_data[i]])
        for i in range(2, len(input_data))
        ]
    
    # list containing 1's if current element is greater than previous
    curr_gt_prev = [
        1 if three_sum[i] > three_sum[i - 1]
        else 0
        for i in range(1, len(three_sum))
    ]

    # return no. of occurences
    return sum(curr_gt_prev)


if __name__ == '__main__':
    out = main()
    print(out)