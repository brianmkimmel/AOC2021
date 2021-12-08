def find_segments(data):
    # digit : segment count
    # 0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6
    segments = {'a':'','b':'','c':'','d':'','e':'','f':'','g':''}
    digits = {'0':'','1':'':'2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':''}
    for digit in data:
        if len(digit) == 2:
            digits['1'] = digit
        elif len(digit) == 4:
            digits['4'] = digit
        elif len(digit) == 3:
            digits['7'] = digit
        elif len(digit) == 7:
            digits['8'] = digit
    


if __name__ == "__main__":
    test = True
    part1 = False
    if test:
        input_filename = 'test_input.txt'
    else:
        input_filename = 'input.txt'
    with open(input_filename) as f:
        # returns the values to the right of the pipe
        if part1:
            data = [x[1].split() for x in [x.split('|') for x in (map(lambda x: x.rstrip(),f.readlines()))]]
        else:
            data = [[x[0].split(),x[1].split()] for x in [x.split('|') for x in (map(lambda x: x.rstrip(),f.readlines()))]]
    print(data)
    if part1:
        # count the number times digits 1, 4, 7, or 8 appear
        digit_count = 0
        for row in data:
            for digit in row:
                if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
                    digit_count += 1
        if test:
            assert digit_count == 26
        print(f"Counted {digit_count} 1,4,7, or 8s")
    else:
        for line in data:
            print(line[0])
