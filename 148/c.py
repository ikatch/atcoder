A, B = map(int, input().split())

i = 1

while (A * i) % B != 0:
  i += 1

print(A * i)