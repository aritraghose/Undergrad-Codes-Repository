# Task 3
# DFS

input_file = open("/content/sample_data/input3_4.txt", "r")
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

matrix = dataToGraph(input_data, n)


def DFS(mat, source = 1):
  visited = [False]*(len(mat))
  DFS_helperFunction(mat, visited, source)

  # for multiple disconnected graphs
  for i in range(1, len(visited)):
    if (visited[i] == False):
      DFS_helperFunction(mat, visited, i)

def DFS_helperFunction(mat, visited, source):
  visited[source] = True
  output_file.write(str(source) + " ")
  for vertex in mat[source]:
    if (visited[vertex] == False):
      DFS_helperFunction(mat, visited, vertex)



DFS(matrix)
output_file.close()