# Task 6

input_file = open("/content/sample_data/input6_1.txt", "r")
r, h = input_file.readline().split(" ")
r = int(r)
h = int(h.strip())
input_data = [i.strip() for i in input_file.readlines()]

output_file = open("/content/sample_data/output6_1.txt", "w")


def dataToGraph(grid):
  graph = {}
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if (grid[i][j] == ".") or (grid[i][j] == "D"):
        neighbours = []
        if (i > 0) and (grid[i-1][j] != "#"):
          neighbours.append((i-1, j))
        if (i < len(grid)-1) and (grid[i+1][j] != "#"):
          neighbours.append((i+1, j))
        if (j > 0) and (grid[i][j-1] != "#"):
          neighbours.append((i, j-1))
        if (j < len(grid[i])-1) and (grid[i][j+1] != "#"):
          neighbours.append((i, j+1))
        graph[(i,j)] = neighbours
      else:
        graph[(i,j)] = []
  return graph
        
def dfs_helper_Function(graph, grid, start, visited, count):
  visited.append(start)
  if (grid[start[0]][start[1]] == "D"):
    count += 1
  maxCount = count
  for i in range(len(graph[start])):
    if graph[start][i] not in visited:
      newCount = dfs_helper_Function(graph, grid, graph[start][i], visited, count)
      maxCount = max(maxCount, newCount)
  visited.remove(start)
  return maxCount




def collectMaxDiamond(grid):
  graph = dataToGraph(grid)
  maxCount = 0
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if (i,j) in graph:
        visited = []
        count = 0
        newCount = dfs_helper_Function(graph, grid, (i,j), visited, count)
        maxCount = max(maxCount, newCount)
  return maxCount


output_file.write(str(collectMaxDiamond(input_data)))
output_file.close()
