import sys

input = sys.stdin.readline

num = ["xxxxxx...xx...xx...xx...xx...xxxxxx", "....x....x....x....x....x....x....x", "xxxxx....x....xxxxxxx....x....xxxxx", "xxxxx....x....xxxxxx....x....xxxxxx", "x...xx...xx...xxxxxx....x....x....x", "xxxxxx....x....xxxxx....x....xxxxxx", "xxxxxx....x....xxxxxx...xx...xxxxxx", "xxxxx....x....x....x....x....x....x", "xxxxxx...xx...xxxxxxx...xx...xxxxxx", "xxxxxx...xx...xxxxxx....x....xxxxxx", ".......x....x..xxxxx..x....x......."]

for i in range(0, 7):
  x = input().strip()
  
  if i == 0:
    lst = [""]*((len(x)+1)//6)
    
  for j in range(0, len(x), 6):
    for k in range(j, j+5):
      lst[(j)//6] += x[k]

for x in range(0, len(lst)):
  if lst[x] in num:
    lst[x] = num.index(lst[x])
    
a = lst.index(10)
num1 = ""
num2 = ""

for i in lst[:a]:
  num1 += str(i)
  
for i in lst[a+1:]:
  num2 += str(i)
  
value = str(int(num1)+int(num2))

for k in range(0, 35,  5):
  for z in range(0, len(value)):
    print(num[int(value[z])][k:k+5], end="")
    if z != len(value) - 1:
      print(".", end ="")
  print()
  
