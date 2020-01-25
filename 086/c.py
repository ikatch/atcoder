N = int(input())
count = 0
for i in range(N):
    t, x, y = map(int, input().split())
    if x + y <= t and (x + y) % 2 == t % 2: count += 1
print("YES" if count == N else "NO")
