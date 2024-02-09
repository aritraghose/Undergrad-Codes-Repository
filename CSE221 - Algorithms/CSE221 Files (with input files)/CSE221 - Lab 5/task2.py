# Task 2
# BFS

input_file = open("/content/sample_data/input2_1.txt", "r")
n, m = input_file.readline().split(" ")
n = int(n)
m = int(m.strip())
input_data = input_file.readlines()

output_file = open("/content/sample_data/output_alt.txt", "w")


def dataToGraph(input_data, n):
  mat = [[] for i in range(n+1)]
  for i in range(len(input_data)):
    input_data[i] = input_data[i].strip()
    source, dest = input_data[i].strip().split(" ")
    mat[int(source)].append(int(dest))
    mat[int(dest)].append(int(source))
  return mat

mat = dataToGraph(input_data, n)


def BFS(mat, source = 1):
  visited = [False]*(len(mat))
  visited[source] = True
  BFS_helperFunction(mat, source, visited)

  # for multiple disconnected graphs
  for i in range(1, len(visited)):
    if (visited[i] == False):
      BFS_helperFunction(mat, i, visited)


def BFS_helperFunction(mat, source, visited):
  queue = []
  queue.append(source)

  while(len(queue) != 0):
    visitingNode = queue[0]
    queue.pop(0)
    output_file.write(str(visitingNode) + " ")

    for vertex in mat[visitingNode]:
      if (visited[vertex] == False):
        visited[vertex] = True
        queue.append(vertex)
  


BFS(mat)
output_file.close()

