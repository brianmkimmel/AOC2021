def find_segments(data):
    # digit : segment count
    # 1: 2
    # 7: 3
    # 4: 4
    # 2: 5, 3: 5, 5: 5
    # 0: 6, 6: 6, 9: 6
    # 8: 7
    digits = {'0': '', '1': '', '2': '', '3': '', '4': '',
              '5': '', '6': '', '7': '', '8': '', '9': ''}
    for digit in data:
        if len(digit) == 2:
            digits['1'] = set(digit)
        elif len(digit) == 4:
            digits['4'] = set(digit)
        elif len(digit) == 3:
            digits['7'] = set(digit)
        elif len(digit) == 7:
            digits['8'] = set(digit)
    # Find 3 and 9:
    for digit in data:
        if len(digit) == 5:
            if digits['7'].issubset(set(digit)):
                digits['3'] = set(digit)
        elif len(digit) == 6:
            if digits['4'].issubset(set(digit)):
                digits['9'] = set(digit)
    # find 0:
    for digit in data:
        if len(digit) == 6:
            sdigit = set(digit)
            if sdigit != digits['9']:
                if digits['1'].issubset(sdigit):
                    digits['0'] = sdigit
    # find 6:
    for digit in data:
        if len(digit) == 6:
            sdigit = set(digit)
            if sdigit != digits['0'] and sdigit != digits['9']:
                digits['6'] = sdigit
    # find 5:
    for digit in data:
        if len(digit) == 5:
            sdigit = set(digit)
            if sdigit.issubset(digits['6']):
                digits['5'] = sdigit
    # find 2:
    for digit in data:
        if len(digit) == 5:
            sdigit = set(digit)
            if sdigit != digits['3'] and sdigit != digits['5']:
                digits['2'] = sdigit
    return digits

def get_output(digits, display):
    value = ''
    for d in display:
        for digit in digits:
            if set(d) == digits[digit]:
                value += digit
    return int(value)
if __name__ == "__main__":
    test = False
    part1 = False
    if test:
        input_filename = 'test_input.txt'
    else:
        input_filename = 'input.txt'
    with open(input_filename) as f:
        # returns the values to the right of the pipe
        if part1:
            data = [x[1].split() for x in [x.split('|')
                                           for x in (map(lambda x: x.rstrip(), f.readlines()))]]
        else:
            data = [[x[0].split(), x[1].split()] for x in [x.split('|')
                                                           for x in (map(lambda x: x.rstrip(), f.readlines()))]]
    #print(data)
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
        sum = 0
        for line in data:
            digits = find_segments(line[0])
            value = get_output(digits, line[1])
            sum += value
        print(f"Sum of displayed values: {sum}")
