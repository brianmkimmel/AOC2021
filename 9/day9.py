import pprint
from copy import deepcopy

def map_basins(hmap, test):
  pp = pprint.PrettyPrinter(width=2000)
  rmax = len(hmap)
  cmax = len(hmap[0])
  bmap = [[0 for x in range(0, cmax)] for x in range(0, rmax)]
  if test:
    print(bmap)
  old_bmap = deepcopy(bmap)
  converged = False
  while (converged == False):
    bmap, basins = search_bmap(hmap, rmax, cmax, bmap)
    pp.pprint(bmap)
    if bmap == old_bmap:
      converged = True
    else:
      old_bmap = deepcopy(bmap)
  # Get three largest basins:
  basin_sizes = sorted(list(basins.values()),reverse=True)[:3]
  if test:
    print(basin_sizes)
  basin_mult = 1
  for x in basin_sizes:
    basin_mult = basin_mult * x
  if test:
    assert basin_mult == 1134
  print(f"Three largest basins: {basin_sizes} multiplied together: {basin_mult}")

def search_bmap(hmap, rmax, cmax, bmap):
    current_basin = 1
    basins = {}
    for r in range(0, rmax):
      for c in range(0, cmax):
        point = hmap[r][c]
        if point != 9:
        # find adjacent basins
          adj_bpoints = [] 
          if r != 0:
            adj_bpoints.append(bmap[r-1][c])
        # South
          if r != rmax-1:
            adj_bpoints.append(bmap[r+1][c])
        # West
          if c != 0:
            adj_bpoints.append(bmap[r][c-1])
        # East
          if c != cmax-1:
            adj_bpoints.append(bmap[r][c+1])
          # sort so if multiple basin numbers are adjacent use the lowest first
          for abp in sorted(adj_bpoints):
            if abp != 0:
              if abp in basins:
                basins[abp] += 1
              else:
                basins[abp] = 1
              bmap[r][c] = abp
              break
          else:
            basins[current_basin] = 1
            bmap[r][c] = current_basin
            current_basin += 1
    return bmap, basins


def find_lowpoints(hmap, test):
  lp_sum = 0
  rmax = len(hmap)
  cmax = len(hmap[0])
  for r in range(0,rmax):
    for c in range(0,cmax):
      lowest = True
      point = hmap[r][c]
      adj_points = []
      # North:
      if r != 0:
        adj_points.append(hmap[r-1][c])
      # South
      if r != rmax-1:
        adj_points.append(hmap[r+1][c])
      # West
      if c != 0:
        adj_points.append(hmap[r][c-1])
      # East
      if c != cmax-1:
        adj_points.append(hmap[r][c+1])
      for ap in adj_points:
        if point >= ap:
          lowest = False
      if lowest:
        lp_sum += point+1
  if test:
    assert lp_sum == 15
  print(f"Sum of risk scores: {lp_sum}")

if __name__ == "__main__":
  test = False
  part1 = False
  if test:
    input_filename = 'test_input.txt'
  else:
    input_filename = 'input.txt'

  with open(input_filename) as f:
    hmap = [list(map(int,list(x))) for x in [x.rstrip() for x in f.readlines()]]
  if test:
    print(hmap)
  if part1:
    find_lowpoints(hmap, test)
  else:
    map_basins(hmap, test)