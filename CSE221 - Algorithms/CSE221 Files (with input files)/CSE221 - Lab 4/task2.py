# Task 2

input_file = open("/content/sample_data/input2_1.txt", "r")
input_data = input_file.readlines()
size = int(input_data[0].strip())
arr = [int(i) for i in input_data[1].split(" ")]


def findMax(arr, i = 0, j = size-1):
  if (i == j):
    return arr[i]
  
  mid = (i+j)//2
  leftMax = findMax(arr, i, mid)
  rightMax = findMax(arr, mid+1, j)
  
  if (leftMax > rightMax):
    return leftMax
  else:
    return rightMax
  

ans = findMax(arr)

output_file = open("/content/sample_data/output2_1.txt", "w")
output_file.write(str(ans))
output_file.close()

