# Task 2

input_file = open("/content/sample_data/input2_4.txt", "r")
n, m = input_file.readline().strip().split(" ")
n  = int(n)
m = int(m)

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


output_file = open('/content/sample_data/output2_4.txt', mode = 'w')



def findBestFit(time_slot, lastFinishedTime):
  waitingTime = [0]*len(lastFinishedTime)
  for i in range(len(lastFinishedTime)):
    if lastFinishedTime[i] == -1:
      waitingTime[i] = time_slot[0]
    else:
      waitingTime[i] = time_slot[0] - lastFinishedTime[i]
    if waitingTime[i] < 0: # This person is already working in this time slot
      waitingTime[i] = None

  person_number = None
  current_min = 1e7
  for i in range(len(waitingTime)):
    if waitingTime[i] != None and waitingTime[i] <= current_min:
      current_min = waitingTime[i]
      person_number = i

  return person_number


  
def maxActivities(timings, no_of_people):
  lastFinishedTime = [-1]*no_of_people
  count = 0
  for i in range(len(timings)):
    if (timings[i][2] == False):
      personNumber = findBestFit(timings[i], lastFinishedTime)
      if (personNumber != None):
        lastFinishedTime[personNumber] = timings[i][1]
        timings[i][2] = True
        count += 1

  return count

count = maxActivities(timings, m)

output_file.write(str(count))
output_file.close()