# Task 3

input_file = open("/content/sample_data/input3_2.txt", "r")
output_file = open("/content/sample_data/output3_2.txt", "w")

n, x = input_file.readline().strip().split(" ")
n = int(n)
x = int(x)

coins = [int(i) for i in input_file.readline().strip().split(" ")]


def findFewestCoins(coins, n, targetAmount):
  table = [[int(1e7) for i in range(targetAmount+1)] for j in range(n)]

  for i in range(len(table[0])):
    if (i % coins[0] == 0):
      table[0][i] = i // coins[0]

  for r in range(1, n):
    for c in range(len(table[r])):
      if coins[r] > c:
        table[r][c] = table[r-1][c]
      else:
        table[r][c] = min(table[r-1][c], 1 + table[r][(c - coins[r])])
  
  if (table[n-1][targetAmount] == 0 or table[n-1][targetAmount] == int(1e7)):
    return -1
  else:
    return table[n-1][targetAmount]




requiredCoins = findFewestCoins(coins, n, x)
output_file.write(str(requiredCoins))
output_file.close()