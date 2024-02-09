# Task 4
# Cycle Finding

input_file = open("/content/sample_data/input4_5.txt", "r")
n, m = input_file.readline().split(" ")
n = int(n)
m = int(m.strip())
input_data = input_file.readlines()

output_file = open("/content/sample_data/output4_5.txt", "w")


def dataToGraph(input_data, n):
  mat = [[] for i in range(n+1)]
  for i in range(len(input_data)):
    input_data[i] = input_data[i].strip()
    source, dest = input_data[i].strip().split(" ")
    mat[int(source)].append(int(dest))
  return mat

mat = dataToGraph(input_data, n)


def findCycle(mat, source = 1):
  color = ["R"]*(len(mat))
  isCycle = False
  isCycle = DFS_helperFunction(mat, color, source)

  if (isCycle == False):
    # for multiple disconnected graphs
    for i in range(1, len(color)):
      if (color[i] != "G"):
        isCycle = DFS_helperFunction(mat, color, i)
  
  if (isCycle):
    output_file.write("YES")
  else:
    output_file.write("NO")


def DFS_helperFunction(mat, color, source):
  color[source] = "Y"
  isCycle = False
  for vertex in mat[source]:
    if (color[vertex] == "R"):
      isCycle = DFS_helperFunction(mat, color, vertex)
    elif (color[vertex] == "Y"): # DFS Still Running
      return True
  color[source] = "G"
  return isCycle

findCycle(mat)
output_file.close()