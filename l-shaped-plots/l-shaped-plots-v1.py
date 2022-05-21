debug = False

"""
(a) xxxx  (b) xxxx  (c)    x  (d) x    
       x      x         xxxx      xxxx

(e)   xx  (f) xx    (g) x     (h)  x
       x      x         x          x
       x      x         x          x
       x      x         xx        xx
"""

def get_segment_length(data,y,x,dy,dx):
    h = len(data)
    w = len(data[y])
    length = 0
    while data[y][x] == 1:
        length += 1
        y += dy
        x += dx
        if y < 0 or x < 0 or y >= h or x >= w:
            return length
    return length    

def traverse_l(data,y,x):
    # Is this a corner? If not, return a zero and leave a potential L to be found later
    found = 0    
    o_left = get_segment_length(data,y,x,0,-1)
    o_down = get_segment_length(data,y,x,1,0)
    o_right = get_segment_length(data,y,x,0,1)
    o_up = get_segment_length(data,y,x,-1,0)
    left = o_left
    down = o_down
    while left >= 4 and down >= 2:
        if debug: print(f"Corner ({y},{x}) left {left} down {down}")
        found += 1
        left = left - 2
        down = down - 1
    left = o_left
    down = o_down
    while left >= 2 and down >= 4:
        if debug: print(f"Corner ({y},{x}) left {left} down {down}")
        found += 1
        left = left - 1
        down = down - 2
    left = o_left
    up = o_up
    while left >= 4 and up >= 2:
        if debug: print(f"Corner ({y},{x}) left {left} up {up}")
        found += 1
        left = left - 2
        up = up - 1
    left = o_left
    up = o_up
    while left >= 2 and up >= 4:
        if debug: print(f"Corner ({y},{x}) left {left} up {up}")
        found += 1
        left = left - 1
        up = up - 2
    right = o_right
    down = o_down
    #if y==2 and x==0: breakpoint()
    while right >= 4 and down >= 2:
        if debug: print(f"Corner ({y},{x}) right {right} down {down}")
        right = right - 2
        down = down - 1
        found += 1
    right = o_right
    down = o_down
    while right >= 2 and down >= 4:
        if debug: print(f"Corner ({y},{x}) right {right} down {down}")
        right = right - 1
        down = down - 2
        found += 1
    right = o_right
    up = o_up
    while right >= 4 and up >= 2:
        if debug: print(f"Corner ({y},{x}) right {right} up {up}")
        right = right - 2
        up = up - 1
        found += 1    
    right = o_right
    up = o_up
    while right >= 2 and up >= 4:
        if debug: print(f"Corner ({y},{x}) right {right} up {up}")
        right = right - 1
        up = up - 2
        found += 1    
    return found

def work(data):
    l = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 1: # Is this a corner?
                l = l + traverse_l(data,y,x)
    return l

def stdin():
    tests_to_read = int(input())
    row_from = 1
    tests_done = 0
    while tests_done < tests_to_read:
        rows, cols = input().split()
        rows = int(rows)
        cols = int(cols)
        grid = []
        for _ in range(rows):
            grid.append(input()+"\n")
        data = [[int(n) for n in line.split()] for line in grid]
        result = work(data)
        tests_done += 1
        print(f"Case #{tests_done}: {result}")
        row_from = row_from + rows + 1

def filein(filename):
    global debug
    with open(filename, "r") as f:
        raw = f.read().splitlines()
    tests_to_read = int(raw[0])
    row_from = 1
    tests_done = 0
    while tests_done < tests_to_read:
        rows, cols = raw[row_from].split()
        rows = int(rows)
        cols = int(cols)
        data = [[int(n) for n in line.split()] for line in raw[row_from+1:row_from+1+rows]]
        result = work(data)
        tests_done += 1
        print(f"Case #{tests_done}: {result}")
        row_from = row_from + rows + 1

filein("./l-shaped-plots/ts2_input.txt")
