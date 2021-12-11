from copy import deepcopy
from pprint import pp
def process_octopi(data):
    # increment all points:
    for r in range(len(data)):
        for c in range(len(data[r])):
            data[r][c] += 1

    # flash octopi
    old_data = deepcopy(data)
    convergence = False
    flash_count = 0
    while (convergence == False):
        #pp(data)
        max_r = len(data)
        for r in range(max_r):
            max_c = len(data[r])
            for c in range(max_c):
                if data[r][c] > 9:
                    data[r][c] = 0
                    flash_count += 1
                    fminc = c - 1
                    fmaxc = c + 1
                    fminr = r - 1
                    fmaxr = r + 1
                    if r == 0:
                        fminr = 0
                    elif r == max_r-1:
                        fmaxr = max_r-1
                    if c == 0:
                        fminc = 0
                    elif c == max_c-1:
                        fmaxc = max_c-1
                    #print(f"r: {r}, c: {c}, fminr,fminc: {fminr},{fminc} fmaxr,fmaxc: {fmaxr},{fmaxc}")
                    for fr in range(fminr, fmaxr+1):
                        for fc in range(fminc, fmaxc+1):
                            #print(f"fr, fc: {fr},{fc}")
                            try:
                                if data[fr][fc] != 0:
                                    data[fr][fc] += 1
                            except Exception as e:
                                print(r,c,fr,fc,e)
        if data == old_data:
            convergence = True
        else:
            old_data = deepcopy(data)
    return data, flash_count

if __name__ == "__main__":
    test = False
    part1 = False
    if test:
        input_filename = 'test_input.txt'
    else:
        input_filename = 'input.txt'

    with open(input_filename) as f:
        data = [list(map(int, x)) for x in map(list,[x.rstrip() for x in f.readlines()])]
    if part1:
        flash_count = 0
        for x in range(100):
            data, count = process_octopi(data)
            flash_count += count
        print(f"Total flashes: {flash_count}")
        if test:
            assert flash_count == 1656
    else:
        all_zeros = [[0 for x in range(len(data[0]))] for x in range(len(data))]
        cycle = 0
        while(data != all_zeros):
            cycle += 1
            data, count = process_octopi(data)
        else:
            print(cycle)
