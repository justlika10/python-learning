a = 0
b = 1
n = int(input())    

for i in range(1, n+1):
  a, b = b, a + b
  print(a)
