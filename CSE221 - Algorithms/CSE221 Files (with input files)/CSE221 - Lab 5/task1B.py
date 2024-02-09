# Task 1(b)

input_file = open("/content/sample_data/input1b_3.txt", "r")
n, m = input_file.readline().split(" ")
n = int(n)
m = int(m.strip())
input_data = input_file.readlines()

output_file = open("/content/sample_data/output1b_3.txt", "w")

nodes = n
edges = m
input = [[int(j) for j in input_data[i].strip().split(" ")] for i in range(len(input_data))]

mat = [[0 for i in range(nodes+1)] for j in range(nodes+1)]


for i in range(len(input)):
  if (mat[input[i][0]][input[i][1]] == 0):
    mat[input[i][0]][input[i][1]] = input[i][2]
  else:
    mat[input[i][0]][input[i][1]] = [mat[input[i][0]][input[i][1]], input[i][2]]


ans_str = ""
for i in range(len(mat)):
  ans_str += (f"{i} : ")
  for j in range(len(mat[i])):
    if (mat[i][j]) != 0:
      if (type(mat[i][j]) == list):
        for k in range(len(mat[i][j])):
          ans_str += (f"({j},{mat[i][j][k]}) ")
      else:
        ans_str += (f"({j},{mat[i][j]}) ")
  if (i != len(mat)-1):
    ans_str += "\n"

output_file.write(ans_str)
output_file.close()