def show(arr):
    for vector in arr:
        for elem in vector:
            print(elem, end = ' ')
        print()
    print()
        
def draw_line(matrix, pos1, pos2):
    x0, x1 = pos1
    y0, y1 = pos2
    deltax = abs(x1 - x0)
    deltay = abs(y1 - y0)
    error = 0
    deltaerr = deltay
    y = y0
    diry = y1 - y0
    if diry > 0:
        diry = 1
    if diry < 0:
        diry = -1
    print(x0, x1)
    for x in range(x0, x1 + 1):
        matrix[x][y] = '*'
        error = error + deltaerr
        if 2 * error >= deltax:
            y += diry
            error -= deltax

def draw_circle(matrix, R, X1, Y1):
    x = 0
    y = R
    delta = 1 - 2 * R
    error = 0
    while y >= 0:
        matrix[X1 + x][Y1 + y] = '*'
        matrix[X1 + x][Y1 - y] = '*'
        matrix[X1 - x][Y1 + y] = '*'
        matrix[X1 - x][Y1 - y] = '*'
        error = 2 * (delta + y) - 1
        if delta < 0 and error <= 0:
            x += 1
            delta += 2 * x + 1
            continue
        if delta > 0 and error > 0:
            y -= 1
            delta -= 2 * y + 1
            continue
        x += 1
        delta += 2 * (x - y)
        y -= 1

matrix = [['.' for _ in range(10)] for __ in range(10)]
show(matrix)
#draw_line(matrix, [0, 5], [7, 8])
draw_circle(matrix, 3, 4, 5)
show(matrix)
