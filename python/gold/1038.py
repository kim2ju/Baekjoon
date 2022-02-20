from itertools import combinations
import sys

input = sys.stdin.readline

N = int(input())
num_list = []

def findDecreaseNum() :
  for i in range(1, 11):
    for combination in combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], i):
      combination = list(combination)
      combination.reverse()
      num_list.append(int(''.join(map(str, combination))))

  num_list.sort()

if N >= 1023:
  print(-1)

else:
  findDecreaseNum()
  print(num_list[N])
  
