# Task 3

import heapq

input_file = open("/content/sample_data/input3_2.txt", "r")
n, m = input_file.readline().split(" ")
n = int(n)
m = int(m.strip())
input_data = input_file.readlines()


output_file = open("/content/sample_data/output3_2.txt", "w")

def dataToAdjList(data, n):
  adjList = [[] for i in range(n+1)]
  for i in range(len(data)):
    temp = data[i].strip().split(" ")
    source = int(temp[0])
    dest = int(temp[1])
    weight = int(temp[2])
    adjList[source].append((dest, weight))
  return adjList
  

adjList = dataToAdjList(input_data, n)

def dijkstra_maxDanger(adjList, source):
  distances = [1e7 for i in range(len(adjList))]
  distances[source] = 0
  queue = []
  queue.append((0, source))

  while (len(queue) != 0):
    distance, vertex = heapq.heappop(queue)
    for neighbour in adjList[vertex]:
      dist = max(distance, neighbour[1])
      if (dist < distances[neighbour[0]]):
        distances[neighbour[0]] = dist
        heapq.heappush(queue, (dist, neighbour[0]))

  for i in range(1, len(distances)):
    if (distances[i] == 1e7):
      distances[i] = "Impossible"
  return distances


def findMinimumDangerLevel(adjList, source, destination):
  distances = dijkstra_maxDanger(adjList, source)
  output_file.write(str(distances[destination]))


findMinimumDangerLevel(adjList, 1, n)
output_file.close()