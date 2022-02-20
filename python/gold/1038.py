from itertools import combinations
import sys

input = sys.stdin.readline

N = int(input())
num_list = []

def findDecreaseNum() :
  for i in range(1, 11):
    for combination in combinations(['9', '8', '7', '6', '5', '4', '3', '2', '1', '0'], i):
      num_list.append(int(''.join(combination)))

  num_list.sort()

if N >= 1023:
  print(-1)

else:
  findDecreaseNum()
  print(num_list[N])
  
