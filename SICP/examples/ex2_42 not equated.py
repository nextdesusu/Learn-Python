def enumerate_interval(from_, to):
    return list(range(from_, to + 1))

def map_(func, seq):
    return list(map(func, seq))

def flatmap(func, seq):
    res = []
    for elem1 in seq:
        if isinstance(elem1, list):
            for elem2 in flatmap(func, elem1):
                res.append(elem2)
        else:
            res.append(func(elem1))
    return res

def accumulate(op, initial, sequence):
    if not len(sequence):
        return initial
    return op(sequence[0], accumulate(op, initial, sequence[1::]))

def filter_(func, seq):
    return list(filter(func, seq))

def list_(*args):
    return list(args)

def queens(board_size):
    
    def adjoin_position(i, k, j):
        return list(i, j)
    
    def safe(k, position):
        
        def queens_safe(queen_count, rest_rows):
            
            def queen_safe(col, row):
                last_col = k
                last_row = position[0]
                return not last_row == row and not abs(last_row - row) == abs(last_col - col)
            
            if not rest_rows:
                return True
            
            if queen_safe(queen_count, rest_rows[0]):
                return queens_safe(queen_count - 1, rest_rows[1::])
            
            else:
                return False
        
        return queens_safe(k - 1, positions[1::])
    
    empty_board = list()
    
    def queen_cols(k):
        if k == 0:
            return empty_board
        return filter_(lambda positions: safe(k, positions),
                       flatmap(lambda rest_of_queens: map_(lambda new_row: adjoin_position(new_row, k, rest_of_queens),
                                                           enumerate_interval(1, board_size)), queen_cols(k - 1)))
                       
    return queen_cols(board_size)

def queens_(board_size):
    
    def safe(r, c, p):
        if previous:
            last_col = p[0]
            last_row = p[1]
            return not last_row == r and not abs(last_row - r) == abs(last_col - c)
        return True
    
    board = [[0 for i in range(board_size)] for j in range(board_size)]
    queen_count = 8
    previous = False
    
    for col in range(len(board)):
        for row in range(len(board[col])):
            if safe(col, row, previous):
                board[col][row] = 1
                previous = (col, row)
                queen_count -= 1
                
    return board

def safe(k, position):

    def queens_safe(queen_count, rest_rows):

        def queen_safe(col, row):
            last_col = k
            last_row = position[0]
            return not last_row == row and not abs(last_row - row) == abs(last_col - col)

        if not rest_rows:
            return True

        if queen_safe(queen_count, rest_rows[0]):
            return queens_safe(queen_count - 1, rest_rows[1::])

        else:
            return False

    return queens_safe(k - 1, positions[1::])
    
for col in queens_(4):
    print(col)