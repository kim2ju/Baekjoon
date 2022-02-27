N, K = map(int, input().split())

num_list = [i for i in range(1, N+1)]
pop_num = 0
result=[]

for i in range(1, N+1):
  pop_num = (pop_num - 1 + K) % len(num_list)
  result.append(num_list.pop(pop_num))

print('<'+', '.join(map(str, result))+'>')
