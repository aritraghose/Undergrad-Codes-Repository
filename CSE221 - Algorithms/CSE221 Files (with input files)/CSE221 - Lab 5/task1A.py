# Task 1(a)

input_file = open("/content/sample_data/input1a_2.txt", "r")
n, m = input_file.readline().split(" ")
n = int(n)
m = int(m.strip())
input_data = input_file.readlines()

output_file = open("/content/sample_data/output1a_2.txt", "w")

nodes = n
edges = m
input = [[int(j) for j in input_data[i].strip().split(" ")] for i in range(len(input_data))]

mat = [[0 for i in range(nodes+1)] for j in range(nodes+1)]


for i in range(len(input)):
  mat[input[i][0]][input[i][1]] = input[i][2]

for i in range(len(mat)):
  for j in range(len(mat[i])):
    output_file.write(str(mat[i][j]) + " ")
  output_file.write("\n")

output_file.close()