def main(input_path: str):
    with open(input_path, 'r') as file:
        input_data = [string.strip('\n').split() for string in file.readlines()]
    
    steps = {
        'forward': 0,
        'down': 0,
        'up': 0
    }

    # direction:step-pairs
    for direction_step in input_data:
        steps[direction_step[0]] += int(direction_step[1])

    print(steps)
    return steps['forward'] * (steps['down'] - steps['up'])

if __name__ == '__main__':
    input_path = 'input1.txt'
    out = main(input_path)
    print(out)