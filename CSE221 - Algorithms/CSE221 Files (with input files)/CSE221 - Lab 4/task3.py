# Task 3

input_file = open("/content/sample_data/input3_3.txt", "r")
input_data = input_file.readlines()
n = int(input_data[0].strip())
arr = [int(i) for i in input_data[1].split(" ")]



def inversionCount(arr, left = 0, right = len(arr)-1):
  if (left == right):
    return 0
  
  mid = (left+right)//2
  count = 0

  count += inversionCount(arr, left, mid)
  count += inversionCount(arr, mid+1, right)
  count += inversionsDuringMerge(arr, left, mid, right)
  return count

def inversionsDuringMerge(arr, left, mid, right):
  i = left
  j = mid + 1
  temp = [0]*(right-left+1)
  k = 0
  count = 0

  while (i <= mid and j <= right):
    if (arr[i] > arr[j]):
      count += (mid-i+1)
      temp[k] = arr[j]
      k += 1
      j += 1
    else:
      temp[k] = arr[i]
      k += 1
      i += 1
  
  while (i <= mid):
    temp[k] = arr[i]
    k += 1
    i += 1
  
  while (j <= right):
    temp[k] = arr[j]
    k += 1
    j += 1
  
  m = left
  for i in range(len(temp)):
    arr[m] = temp[i]
    m += 1

  return count


  
ans = inversionCount(arr)

output_file = open("/content/sample_data/output3_3.txt", "w")
output_file.write(str(ans))
output_file.close()
