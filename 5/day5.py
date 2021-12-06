import pprint

def plot_lines(points, start, end, horiz):
    current_x = start[0]
    current_y = start[1]
    while (current_x != end[0] or current_y != end[1]):
        #print(f"current_x: {current_x}, current_y: {current_y}")
        try:
            points[current_y][current_x] += 1
        except Exception as e:
            print(f"{e} current_x: {current_x}, current_y: {current_y} end x: {end[0]}, end y: {end[1]}")
        if end[0]-current_x > 0:
            current_x += 1
        elif end[0]-current_x < 0:
            current_x -= 1
        if end[1]-current_y > 0:
            current_y += 1
        elif end[1]-current_y < 0:
            current_y -= 1
    points[end[1]][end[0]] += 1

    return points

if __name__ == "__main__":
    ppr = pprint.PrettyPrinter(indent=4)
    test = False
    if test:
        input_filename = 'test_input.txt'
    else:
        input_filename = 'input.txt'
    with open(input_filename) as f:
        raw_data = f.readlines()
    data = []
    for line in raw_data:
        data.append(line.replace(' ','').rstrip().split('->'))
    #print(data)
    points = []
    for line in data:
        pt1 = None
        pt2 = None
        for strpoint in line:
            point = list(map(int,strpoint.split(',')))
            #print(point)
            if pt1 is None:
                pt1 = point
            else:
                pt2 = point
        points.append((pt1,pt2))
    #print(points)
    # filter out diagonals
    #points = list(filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], points))
    #print(points)
    # find max x, max y
    max_x = 0
    max_y = 0
    for pp in points:
        for pt in pp:
            if pt[0] > max_x:
                max_x = pt[0]
            if pt[1] > max_y:
                max_y = pt[1]
    print(max_x,max_y) 
    #create empty map
    floor_map = [[0 for x in range(0,max_y+2)] for x in range(0,max_x+2)]
    #ppr.pprint(floor_map)
    for pp in points:
        start = pp[0]
        end = pp[1]
        floor_map = plot_lines(floor_map, start, end, True)

    #ppr.pprint(floor_map)
    intersections = 0
    for y in range(0,max_y+1):
        for x in range(0,max_x+1):
            if floor_map[y][x] > 1:
                intersections += 1
    print(f"Intersecting lines: {intersections}")

