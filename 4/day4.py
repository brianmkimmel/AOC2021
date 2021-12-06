def search_board(board, number):
    rn = 0
    cn = 0
    for r in board:
        cn = 0
        for c in r:
            if int(c) == number:
                return(rn,cn)
            cn += 1
        rn += 1
    return (None, None)

def find_bingo(board_marks):
    bingos = []
    for board in board_marks:
        # find horizontal bingo
        for r in range(0,5):
            if sum(board_marks[board][r]) == 5:
                bingos.append(board)
        for c in range(0,5):
            for r in range(0,5):
                if board_marks[board][r][c] == 0:
                    break
                if r == 4:
                    bingos.append(board)
    return bingos

def sum_unmarked(board, marks):
    unmsum = 0
    for r in range(0,5):
        for c in range(0,5):
            if marks[r][c] == 0:
                unmsum += int(board[r][c])
    return unmsum

def play_bingo(numbers, boards):
    board_marks = {}
    for board in boards:
        board_marks[board] = [[0 for x in range(0,5)] for x in range(0,5)]
    for n in numbers:
        for board in boards:
            r,c = search_board(boards[board], n)
            if r is not None:
                #print(r,c)
                board_marks[board][r][c] = 1
        bingos = find_bingo(board_marks)
        #print(bingos, len(boards),boards.keys())
        print(bingos, len(boards), n)
        for bingo in bingos:
            if len(boards) > 1:
                if bingo in boards: boards.pop(bingo)
                if bingo in board_marks: board_marks.pop(bingo)
            else:
                unmsum = sum_unmarked(boards[bingo], board_marks[bingo])
                print(board_marks)
                print(f"Found bingo on board {bingo}, number called {n}, unmarked sum {unmsum}, multiplied: {n*unmsum}")
                break
        else:
            continue
        break
    #print(board_marks)
    


if __name__ == "__main__":
    test = False
    if test:
        data_file = 'test_input.txt'
    else:
        data_file = 'input.txt'
    with open(data_file) as f:
        numbers = list(map(int,f.readline().rstrip().split(',')))
        f.readline()
        boards_raw = f.readlines()
    #print(numbers)
    #print(boards_raw)
    boards = {}
    x = 0
    boards[0] = []
    for line in boards_raw:
        line = line.rstrip()
        if line != '':
            boards[x].append(line.split())
        else:
            x += 1
            boards[x] = []
    #print(len(boards))
    #print(boards)
    play_bingo(numbers, boards)

