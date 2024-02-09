
# test
n = 8
m = 7
edges = [[2, 4, 0], [4, 5, 0], [3, 6, 0], [4, 7, 0], [3, 1, 0], [2, 7, 0], [6, 2, 0]]

# end

parent = [i for i in range(n+1)]
rank = [1 for i in range(n+1)]
circleCounter = [1 for i in range(n+1)]

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
    circleCounter[parent_v] += circleCounter[parent_u]
  elif rank[parent_u] > rank[parent_v]:
    parent[parent_v] = parent_u
    circleCounter[parent_u] += circleCounter[parent_v]
  else:
    parent[parent_v] = parent_u
    rank[parent_u] += 1
    circleCounter[parent_u] += circleCounter[parent_v]



for i in range(len(edges)):
  join(edges[i][0], edges[i][1])
  print(circleCounter[root(edges[i][0])])