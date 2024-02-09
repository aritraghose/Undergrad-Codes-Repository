# Task 1

input_file = open("/content/sample_data/input1_3.txt", "r")
n = int(input_file.readline().strip())
timings = []

for line in input_file.readlines():
  start, end = line.strip().split(" ")
  timings.append([int(start), int(end), False])


def quickSort(arr, low, high):
  if (low < high):
    pi = partition(arr, low, high)
    quickSort(arr, low, pi-1)
    quickSort(arr, pi+1, high)


def partition(arr, low, high):
  pivot = arr[high][1]
  i = low - 1
  for j in range(low, high):
    if (arr[j][1] <= pivot):
      i += 1
      arr[i] , arr[j] = arr[j], arr[i]
  arr[i+1], arr[high] = arr[high], arr[i+1]
  return i+1

quickSort(timings, 0, len(timings)-1) # sorting based on finish time


output_file = open('/content/sample_data/output1_3.txt', mode = 'w')

count = 0
works = ""
lastFinishedTime = -1
for i in range(len(timings)):
  if (timings[i][0] >= lastFinishedTime) and (timings[i][2] == False):
    count += 1
    timings[i][2] = True
    lastFinishedTime = timings[i][1]
    works += f"\n{timings[i][0]} {timings[i][1]}"

output_file.write(str(count))
output_file.write(works)
output_file.close()