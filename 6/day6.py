
def process_fish(fish):
  new_fish = [0 for x in range(0,9)]
  # generate new fish:
  if fish[0] > 0:
    new_fish[8] += fish[0]
    new_fish[6] += fish[0]
  # move all other fish down one spot
  for f in range(1,9):
    new_fish[f-1] += fish[f]
  return new_fish


if __name__ == "__main__":
  test = False
  if test:
    input_filename = 'test_input.txt'
  else:
    input_filename = 'input.txt'
  with open(input_filename) as f:
    data = list(map(int,f.readline().split(',')))
  print(data)
  fish = [0 for x in range(0,9)]
  for d in data:
    fish[d] += 1
  print(fish)
  for x in range(0,256):
    fish = process_fish(fish)
    print(sum(fish))