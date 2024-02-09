# Task 2

input_file = open("/content/sample_data/input2_4.txt", "r")
output_file = open("/content/sample_data/output2_4.txt", "w")
n = int(input_file.readline().strip())


def findWays(n, waysStorge):
  if (waysStorage[n] != None):
    return waysStorage[n]
  elif (n == 0) or (n == 1):
    waysStorage[n] = 1
    return 1
  waysStorage[n] = findWays(n-1, waysStorage) + findWays(n-2, waysStorage)
  return waysStorage[n]


waysStorage = [None for i in range(n+1)]
ways = findWays(n, waysStorage)
output_file.write(str(ways))
output_file.close()