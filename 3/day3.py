from copy import deepcopy

def count_columns(data: list) -> dict:
  columns = {}
  for row in data:
    x = 0
    for c in row:
      if x not in columns:
        columns[x] = {"1": 0, "0": 0}
      if c == "1":
        columns[x]["1"] += 1
      else:
        columns[x]["0"] += 1
      x += 1
  return columns

def find_gamma(columns: dict) -> list:
  gamma = []
  epsilon = []
  for x in columns:
    one = columns[x]["1"]
    zero = columns[x]["0"]
    if one > zero:
      gamma.append('1')
      epsilon.append('0')
    else:
      gamma.append('0')
      epsilon.append('1')
  return [int(''.join(gamma),2),int(''.join(epsilon),2)]

def count_filter(data: list, c: int) -> list:
  #print(f"Starting row count: {len(data)}")
  one = 0
  zero = 0
  for row in data:
    if row[c] == "1":
      one += 1
    else:
      zero += 1
  print(f"In column {c} count {one} ones and {zero} zeros")
  # filter rows
  if zero > one:
    keep_val = "0"
  else:
    keep_val = "1"
  data = list(filter(lambda row: row[c] == keep_val, data))
  #print(f"ending row count: {len(data)}")
  return data


def count_filter_co2(data: list, c: int) -> list:
  #print(f"Starting row count: {len(data)}")
  if len(data) == 1:
    return data
  one = 0
  zero = 0
  for row in data:
    if row[c] == "1":
      one += 1
    else:
      zero += 1
  print(f"In column {c} count {one} ones and {zero} zeros")
  # filter rows
  if zero > one:
    keep_val = "1"
  elif zero == one:
    keep_val = "0"
  else:
    keep_val = "0"
  data = list(filter(lambda row: row[c] == keep_val, data))
  #print(f"ending row count: {len(data)}")
  return data

def find_lsr(data: list) -> list:
  data2 = deepcopy(data)
  #find most common value in current column
  for c in range(0,len(data[0])):
    data = count_filter(data,c)
    data2 = count_filter_co2(data2, c)
  oxy = int(''.join(data[0]),2)
  co2 = int(''.join(data2[0]),2)
  return [oxy, co2]


if __name__ == "__main__":
  with open('input.txt') as f:
    data = list(map(list,map(str.rstrip, f.readlines())))
  columns = count_columns(data)
  #print(columns)
  gamma, epsilon = find_gamma(columns)
  print(f"Foung gamma: {gamma}, epsilon: {epsilon} multiplied together: {gamma*epsilon}")
  oxy, co2 = find_lsr(data)
  print(f"Found oxygen generator rating: {oxy}, CO2 scrubber rating: {co2}, multiplied together: {oxy*co2}")