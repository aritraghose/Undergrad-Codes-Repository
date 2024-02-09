# Task 5
# Shortest Path

input_file = open("/content/sample_data/input5_5.txt", "r")
n, m, d = input_file.readline().split(" ")
n = int(n)
m = int(m)
d = int(d.strip())
input_data = input_file.readlines()

output_file = open("/content/sample_data/output5_5.txt", "w")


def dataToGraph(input_data, n):
  mat = [[] for i in range(n+1)]
  for i in range(len(input_data)):
    input_data[i] = input_data[i].strip()
    source, dest = input_data[i].strip().split(" ")
    mat[int(source)].append(int(dest))
    mat[int(dest)].append(int(source))
  return mat

mat = dataToGraph(input_data, n)


def findShortestPath(mat, destination, source = 1):
  visited = [False]*(len(mat))
  level = [-1]*(len(mat))
  parent = [None]*(len(mat))

  visited[source] = True
  level[source] = 0
  BFS_helper_function(mat, source, visited, parent, level)

  # for multiple disconnected graphs
  for i in range(1, len(visited)):
    if (visited[i] == False):
      BFS_helper_function(mat, i, visited, parent, level)

  shortestPathDetails = f"Time: {level[destination]}\nShortest Path: "
  path = ""
  while(destination != None):
    path = str(destination) + " " + path
    destination = parent[destination]
  shortestPathDetails += path
  output_file.write(shortestPathDetails)


def BFS_helper_function(mat, source, visited, parent, level):
  queue = []
  queue.append(source)

  while(len(queue) != 0):
    visitingNode = queue[0]
    queue.pop(0)

    for vertex in mat[visitingNode]:
      if (visited[vertex] == False):
        visited[vertex] = True
        parent[vertex] = visitingNode
        level[vertex] = level[visitingNode] + 1
        queue.append(vertex)


findShortestPath(mat, d)
output_file.close()