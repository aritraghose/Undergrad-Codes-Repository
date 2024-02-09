# Task 2
import heapq

input_file = open("/content/sample_data/input2_3.txt", "r")
n, m = input_file.readline().split(" ")
n = int(n)
m = int(m.strip())
input_data = input_file.readlines()
s, t = (input_data[len(input_data)-1]).strip().split(" ")
s = int(s)
t = int(t)

output_file = open("/content/sample_data/output2_3.txt", "w")

def dataToAdjList(data, n):
  adjList = [[] for i in range(n+1)]
  for i in range(len(data)-1):
    temp = data[i].strip().split(" ")
    source = int(temp[0])
    dest = int(temp[1])
    weight = int(temp[2])
    adjList[source].append((dest, weight))
  return adjList
  

adjList = dataToAdjList(input_data, n)

def shortestPathsFromSource(adjList, source):
  distances = [1e7 for i in range(len(adjList))]
  distances[source] = 0
  queue = []
  queue.append((0, source))

  while (len(queue) != 0):
    distance, vertex = heapq.heappop(queue)
    for neighbour in adjList[vertex]:
      v2v_distance = distance + neighbour[1]
      if (v2v_distance < distances[neighbour[0]]):
        distances[neighbour[0]] = v2v_distance
        heapq.heappush(queue, (v2v_distance, neighbour[0]))

  for i in range(1, len(distances)):
    if (distances[i] == 1e7):
      distances[i] = -1
  return distances



def alice_meets_bob(adjList, s, t):
  alicePaths = shortestPathsFromSource(adjList, s)
  bobPaths = shortestPathsFromSource(adjList, t)
  meetingNode = None
  timeTaken = 1e7

  for i in range(1, len(alicePaths)):
    if (alicePaths[i] == -1):
      continue
    if (bobPaths[i] == -1):
      continue
    timeTook = max(alicePaths[i], bobPaths[i])
    if (timeTook < timeTaken):
      timeTaken = timeTook
      meetingNode = i
  
  if (meetingNode == None):
    output_file.write("Impossible")
  else:
    output_file.write(f"Time {timeTaken}\nNode {meetingNode}")

  

alice_meets_bob(adjList, s, t)
output_file.close()