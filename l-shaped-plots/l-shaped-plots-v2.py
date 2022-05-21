#import time
debug = False

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

def count_l(long, short):
    # Default to sizing the L based on the long side
    long_length_usable = abs(long) // 2 * 2
    short_length_usable = long_length_usable // 2
    if short_length_usable > abs(short): # Check if the short side will force a shorter L
        short_length_usable = abs(short)
        long_length_usable = short_length_usable * 2
    if debug: print("   count_l long",long_length_usable,"short",short_length_usable,"usable Ls",short_length_usable-1)
    return short_length_usable-1

def work(data):
    # Segments stored as a tuple: y1,x1,y2,x2
    horizontal = [] # Segments going across a row
    vertical = [] # Segments going down a column
    h = len(data)
    w = len(data[0])
    # Find the horizontal segments
    for y in range(h):
        x = 0
        while x < w:
            if data[y][x] == 1:
                length = get_segment_length(data, y, x, 0, 1)
                if length > 1:
                    horizontal.append((y,x,y,x+length-1))
                x+=length
            else:
                x+=1
    # Find the vertical segments
    for x in range(w):
        y = 0
        while y < h:
            if data[y][x] == 1:
                length = get_segment_length(data, y, x, 1, 0)
                if length > 1:
                    vertical.append((y,x,y+length-1,x))
                y+=length
            else:
                y+=1
    # Process segments, searching for points of intersection
    if debug: print("Horizontal\n",horizontal)
    if debug: print("Vertical\n",vertical)
    # Iterate through horizontal segments, find vertical segments that intersect
    total = 0
    for horiz in horizontal:  # y,  x1, y,  x2
        for vert in vertical: # y1, x,  y2, x
            if horiz[0] >= vert[0] and horiz[0] <= vert[2] and horiz[1] <= vert[1] and horiz[3] >= vert[1]:
                # Intersection... count how many L's appear
                point = (horiz[0],vert[1])
                if debug: print("Intersection at (y,x) = ",point,"hor",horiz,"ver",vert)
                # Check left-up
                if point[0]-vert[0]+1 >= 4 and point[1]-horiz[1]+1 >= 2: # Long end up
                    if debug: print(" - Up / Left      = ",point[0]-vert[0]+1, point[1]-horiz[1]+1)
                    long = point[0]-vert[0]+1
                    short = point[1]-horiz[1]+1
                    total += count_l(long, short)
                if point[0]-vert[0]+1 >= 2 and point[1]-horiz[1]+1 >= 4: # Long end left
                    if debug: print(" - Left / up      = ",point[0]-vert[0]+1, point[1]-horiz[1]+1)
                    long = point[1]-horiz[1]+1
                    short = point[0]-vert[0]+1
                    total += count_l(long, short)
                # Check up-right
                if point[0]-vert[0]+1 >= 4 and horiz[3]-point[1]+1 >= 2: # Long end up
                    if debug: print(" - Up / right     = ",point[0]-vert[0]+1, horiz[3]-point[1]+1)
                    long = point[0]-vert[0]+1
                    short = horiz[3]-point[1]+1
                    total += count_l(long, short)
                if point[0]-vert[0]+1 >= 2 and horiz[3]-point[1]+1 >= 4: # Long end right
                    if debug: print(" - Right / up     = ",point[0]-vert[0]+1, horiz[3]-point[1]+1)
                    long = horiz[3]-point[1]+1
                    short = point[0]-vert[0]+1
                    total += count_l(long, short)
                # Check right-down
                if vert[2]-point[0]+1 >= 4 and horiz[3]-point[1]+1 >= 2: # Long end down
                    if debug: print(" - Down / right   = ",vert[2]-point[0]+1, horiz[3]-point[1]+1)
                    long = vert[2]-point[0]+1
                    short = horiz[3]-point[1]+1
                    total += count_l(long, short)
                if vert[2]-point[0]+1 >= 2 and horiz[3]-point[1]+1 >= 4: # Long end right
                    if debug: print(" - Right / down   = ",vert[2]-point[0]+1, horiz[3]-point[1]+1)
                    long = horiz[3]-point[1]+1
                    short = vert[2]-point[0]+1
                    total += count_l(long, short)
                # Check down-left
                if vert[2]-point[0]+1 >= 4 and point[1]-horiz[1]+1 >= 2: # Long end down
                    if debug: print(" - Down / left    = ",vert[2]-point[0]+1, point[1]-horiz[1]+1)
                    long = vert[2]-point[0]+1
                    short = point[1]-horiz[1]+1
                    total += count_l(long, short)
                if vert[2]-point[0]+1 >= 2 and point[1]-horiz[1]+1 >= 4: # Long end left
                    if debug: print(" - Left / down   = ",vert[2]-point[0]+1, point[1]-horiz[1]+1)
                    long = point[1]-horiz[1]+1
                    short = vert[2]-point[0]+1
                    total += count_l(long, short)
    return total

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

#t = time.time()
#filein("./l-shaped-plots/sample_ts1_input.txt")
#filein("./l-shaped-plots/ts1_input.txt")
#filein("./l-shaped-plots/ts2_input.txt")
#print(time.time()-t)
stdin()
