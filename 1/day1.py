def parse_input():
  depths = []
  with open('input.txt') as f:
    for line in f:
      depths.append(int(line))
  return depths


def part1(depths):
  # set prev_depth to a large number so it can't increase on the first comparison
  prev_depth = 100000
  increases = 0
  for depth in depths:
    if (depth > prev_depth):
      increases += 1
    prev_depth = depth
  print("Number of increases: ", increases)

def part2(depths):
  # compare sliding windows of 3 depths until end of readings
  window = 0
  end = False
  last_window_sum = 1000000
  increases = 0
  while(window < len(depths)):
    window_sum = sum(depths[window:window+3])
    if window_sum > last_window_sum:
      increases += 1
    window += 1
    last_window_sum = window_sum
  print("Number of window increases ", increases)


depths = parse_input()
part1(depths)
part2(depths)