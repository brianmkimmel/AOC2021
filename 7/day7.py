def fuel_spend1(start, end):
  return abs(start-end)


def fuel_spend2(start, end):
  diff = abs(start-end)
  """
  fuel = 0
  for x in range(1,diff+1):
    fuel += x
  """
  # use gauss sum instead
  return (diff * (diff +1))/2




if __name__ == "__main__":
  test = False
  if test:
    positions = [16,1,2,0,4,2,7,1,2,14]
  else:
    with open('input.txt') as f:
      positions = list(map(int,f.readline().split(',')))
  
  pos = 0
  # start with large value 
  min_diff = 10000000000
  min_pos = 0
  for pos in range(0,max(positions)+1):
    diffs = list(map(fuel_spend2,positions,[pos]*len(positions)))
    #print(diffs)
    if sum(diffs) < min_diff:
      min_diff = sum(diffs)
      min_pos = pos
  print(f"Spend {min_diff} fuel to reach position {min_pos}")