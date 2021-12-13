from tabulate import tabulate

def fold_paper(paper,fold):
  axis, line = fold.split('=')
  line = int(line)
  if axis == 'y':
    # fold rows
    bottom_rows = len(paper) - line
    if bottom_rows > line:
      folds = line
    else:
      folds = bottom_rows
    for r in range(1,folds+1):
      for c in range(len(paper[0])):
        #print(f"Upper: {c},{line-r} {paper[line-r][c]}, Lower: {c},{line+r} {paper[line+r][c]}")
        paper[line-r][c] += paper[line+r][c]
    paper = paper[:line]
  elif axis == 'x':
    #fold columns
    right_columns = len(paper[0]) - line
    if right_columns > line:
      folds = line
    else:
      folds = right_columns
    for c in range(1,folds+1):
      for r in range(len(paper)):
        #print(f"Upper: {line-c},{r} {paper[r][line-c]}, Lower: {line+c},{r} {paper[r][line+c]}")
        paper[r][line-c] += paper[r][line+c]
    paper2 = []
    for row in paper:
      paper2.append(row[:line])
    paper = paper2

  return paper



if __name__ == "__main__":
  test = False
  part1 = False
  if test:
    input_file = 'test_input.txt'
  else:
    input_file = 'input.txt'
  
  with open(input_file) as f:
    points = []
    folds = []
    read_points = True
    for line in f.readlines():
      if line.rstrip() == '':
        read_points = False
        continue
      if read_points:
        points.append(line.rstrip().split(','))
      else:
        folds.append(line.rstrip().split(' ')[2])
    points = [[int(x[0]),int(x[1])] for x in points]
    #print(points, folds)

    # Find max row, column
    max_row = 0
    max_column = 0
    for p in points:
      if p[0] > max_row:
        max_row = p[0]
      if p[1] > max_column:
        max_column = p[1]
    print(f"Max row: {max_row}, Max column: {max_column}")
    paper = [[0 for x in range(max_row+1)] for x in range(max_column+1)]
    #print(paper)
    for p in points:
      paper[p[1]][p[0]] = 1
    #print(paper)
    if part1:
      # Do first fold:
      paper = fold_paper(paper,folds[0])
      #print(paper)
      # count dots:
      dot_count = 0
      for r in range(len(paper)):
        for c in range(len(paper[0])):
          if paper[r][c] != 0:
            dot_count += 1
      print(dot_count)
    else:
      for fold in folds:
        paper = fold_paper(paper,fold)
      for r in range(len(paper)):
        for c in range(len(paper[0])):
          if paper[r][c] != 0:
            paper[r][c] = '#'
          else:
            paper[r][c] = ''
      print(tabulate(paper))