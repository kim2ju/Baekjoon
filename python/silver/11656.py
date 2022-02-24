string = input()
string_list = []

for i in range(len(string)):
  string_list.append(string[i:])

string_list.sort()

for i in string_list:
  print(i)
  
