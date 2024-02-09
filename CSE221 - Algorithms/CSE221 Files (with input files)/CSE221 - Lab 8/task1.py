# Task 1


input_file = open("/content/sample_data/input1_2.txt", "r")
output_file = open('/content/sample_data/output1_2.txt', mode = 'w')
n, m = input_file.readline().strip().split(" ")
n  = int(n)
m = int(m)
edges = []

for i in input_file.readlines():
  u, v, w = i.strip().split(" ")
  edges.append([int(u), int(v), int(w)])

def quickSort(arr, low, high):
  if (low < high):
    pi = partition(arr, low, high)
    quickSort(arr, low, pi-1)
    quickSort(arr, pi+1, high)


def partition(arr, low, high):
  pivot = arr[high][2]
  i = low - 1
  for j in range(low, high):
    if (arr[j][2] <= pivot):
      i += 1
      arr[i] , arr[j] = arr[j], arr[i]
  arr[i+1], arr[high] = arr[high], arr[i+1]
  return i+1



parent = [i for i in range(n+1)]
rank = [1 for i in range(n+1)]


def root(i):
  if parent[i] != i:
    parent[i] = root(parent[i])
  return parent[i]

def join(u, v):
  parent_u = root(u)
  parent_v = root(v)
  if parent_u == parent_v:
    return

  if rank[parent_u] < rank[parent_v]:
    parent[parent_u] = parent_v

  elif rank[parent_u] > rank[parent_v]:
    parent[parent_v] = parent_u
  else:
    parent[parent_v] = parent_u
    rank[parent_u] += 1



def kruskal(edges, n):
  MST = []
  quickSort(edges, 0, len(edges)-1)
  i = 0
  j = 0
  cost = 0
  while (j < n-1):
    u, v, w = tuple(edges[i])
    i += 1
    parent_u = root(u)
    parent_v = root(v)
    if parent_u != parent_v:
      join(parent_u, parent_v)
      cost += w
      j += 1
      MST.append([u, v, w])
  return cost


cost = kruskal(edges, n)
output_file.write(str(cost))
output_file.close()