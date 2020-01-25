A, B, K = map(int, input().split())
if A + B >= K:
    if A >= K:
        A -= K
    else:
        B -= (K - A)
        A = 0
else:
    A, B = 0, 0
print(A, B)