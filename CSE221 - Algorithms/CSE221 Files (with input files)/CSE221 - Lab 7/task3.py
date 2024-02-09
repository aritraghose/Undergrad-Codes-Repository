# Task 3

input_file = open("/content/sample_data/input3_2.txt", "r")
n, m = input_file.readline().strip().split(" ")
n  = int(n)
m = int(m)
input_data = []

for i in input_file.readlines():
  p1 , p2 = i.strip().split(" ")
  input_data.append([int(p1), int(p2)])


parentSet = [i for i in range(n+1)]
circleCounter = [1 for i in range(n+1)]

def root(i):
  if (parentSet[i] == -1):
    return i 
  elif (parentSet[i] == i):
    return -1
  else:
    return root(parentSet[i])

def join(u, v):
  parent_u = root(u)
  parent_v = root(v)
  if (parent_u == -1 and parent_v == -1): # both are not part of any tree/friend circle
    parentSet[v] = u
    parentSet[u] = -1
    circleCounter[u] += 1
  elif (parent_v == -1 and parent_u != -1):
    parentSet[v] = u
    circleCounter[parent_u] += 1
  elif (parent_u == -1 and parent_v != -1):
    parentSet[u] = v
    circleCounter[parent_v] += 1

  else:
    if parent_u != parent_v:
      parentSet[parent_v] = parent_u
      circleCounter[parent_u] += circleCounter[parent_v]


output_file = open('/content/sample_data/output3_2.txt', mode = 'w')

for i in range(len(input_data)):
  join(input_data[i][0], input_data[i][1])
  circle = circleCounter[root(input_data[i][1])]
  output_file.write(str(circle) + "\n")

output_file.close()

