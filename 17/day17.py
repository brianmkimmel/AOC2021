def update_probe(x,y,dx,dy):
    x += dx
    y += dy
    if dx > 0:
        dx -= 1
    elif dx < 0:
        dx += 1
    dy -= 1
    return(x,y,dx,dy)

def check_bounds(x,y,mintx,maxtx,minty,maxty):
    if x > maxtx:
        return False,True
    if y < minty:
        return False,True
    if x >= mintx and x <= maxtx and y >= minty and y <= maxty:
        return True, False
    return False, False
    
if __name__ == "__main__":
    data = "target area: x=257..286, y=-101..-57"
    mintx = 257
    maxtx = 286
    minty = -101
    maxty = -57

    max_ys = []
    for dy in range(6000):
        for dx in range(2000):
            overshot = False
            maxy = 0
            x = 0
            y = 0
            while overshot == False:
                x,y,dx,dy = update_probe(x,y,dx,dy)
                in_target, overshot = check_bounds(x,y,mintx,maxtx,minty,maxty)
                if y > maxy:
                    maxy = y
                if in_target:
                    max_ys.append(maxy)
                    print(maxy)
                    assert False
                if overshot:
                    #print(f"x: {x}, y: {y}, dx: {dx}, dy: {dy}")
                    pass
    print(max_ys)
