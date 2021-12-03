def run_sub(commands: list) -> None:
  position = 0
  depth = 0
  for c in commands:
    if c[0] == 'forward':
      position += c[1]
    elif c[0] == 'down':
      depth += c[1]
    elif c[0] == 'up':
      depth -= c[1]
  print(f"Final hoz pos: {position}, final depth: {depth}, puzzle answer: {position*depth}")

def run_sub2(commands: list) -> None:
  pos = 0
  depth = 0
  aim = 0
  for c in commands:
    if c[0] == 'forward':
      pos += c[1]
      depth += (aim * c[1])
    elif c[0] == 'down':
      aim += c[1]
    elif c[0] == 'up':
      aim -= c[1]
  print(f"Final hoz pos: {pos}, final depth: {depth}, puzzle answer: {pos*depth}")

def parse_input() -> list:
  commands = []
  with open('input.txt') as f:
    for line in f:
      direction, distance = line.split(' ')
      distance = int(distance)
      commands.append([direction, distance])
  return commands

commands = parse_input()
run_sub(commands)
run_sub2(commands)