import math

def find_unmatched(line: list[str]) -> str:
  # delete two character chunks until mismatched chunk appears
  pairs = {'(':')','[':']','{':'}','<':'>'}
  corrupted = False
  illegal_char = ''
  while (corrupted == False):
    for c in range(0,len(line)-1):
      #print(line[c],line[c+1])
      if line[c] in pairs:
        if line[c+1] not in pairs:
          # found match
          if pairs[line[c]] == line[c+1]:
            #print(f"Deleting: {line[c]} {line[c+1]}")
            del line[c+1]
            del line[c]
            break
          else:
            #print(f"Found corrupt? {line[c]} {line[c+1]}")
            corrupted = True
            illegal_char = line[c+1]
            break
    else:
      # line must be incomplete not corrupt
      #print(f"No illegals chars found")
      return "_"
    
  return illegal_char

def score_incomplete(line: list[str]) -> int:
  scores = {'(':1, '[':2, '{':3, '<':4}
  total_score = 0
  for c in reversed(range(len(line))):
    score = scores[line[c]]
    total_score = total_score * 5
    total_score += score
  return total_score



if __name__ == "__main__":
  test = False
  if test:
    input_filename = 'test_input.txt'
  else:
    input_filename = 'input.txt'
  
  with open(input_filename) as f:
    data = list(map(list,[x.rstrip() for x in f.readlines()]))
  scoring = {')':3,']':57,'}':1197,'>':25137,'_':0,'':0}
  score = 0
  line_scores = []
  for line in data:
    illegal = find_unmatched(line)
    if illegal == '_':
      line_scores.append(score_incomplete(line))
    score += scoring[illegal]
  line_scores.sort()
  if test:
    assert score == 26397
    assert line_scores[math.floor(len(line_scores)/2)] == 288957
  print(f"Final score: {score}")
  print(
      f"Line scores: {line_scores} middle score: {line_scores[math.floor(len(line_scores)/2)]}")
    