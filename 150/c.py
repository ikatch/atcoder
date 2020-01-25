import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

A = list(itertools.permutations(range(1, N+1, 1)))

print(abs(A.index(P) - A.index(Q)))