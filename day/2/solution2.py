def main(input_path: str):
    with open(input_path, 'r') as file:
        input_data = [string.strip('\n').split() for string in file.readlines()]
    
    aim = 0
    h_pos = 0
    depth = 0
    for _list in input_data:
        direction, step = _list[0], int(_list[1])
        if direction == 'up':
            aim -= step
        elif direction == 'down':
            aim += step
        elif direction == 'forward':
            h_pos += step
            depth += aim * step
    
    return h_pos * depth


if __name__ == '__main__':
    input_path = 'input1.txt'
    out = main(input_path)
    print(out)