N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())

Ts = [[] for _ in range(K)]
for i, x in enumerate(T):
    k = i % K
    Ts[k].append(x)


def solve(t):
    r, s, p = 0, 0, 0   # player の現時点の手ごとの最大得点

    for x in t[::-1]:   # 相手の手を逆順にして、最終手から探索
        if x == 'r':
            r, s, p = max(s, p), max(p, r), max(r, s) + P
            # 現時点で r を出す場合、次時点で s または p を出す。現時点では引き分けのため、無加点
            # 現時点で s を出す場合、次時点で p または r を出す。現時点では負けのため、無加点
            # 現時点で p を出す場合、次時点で r または s を出す。現時点では勝ちのため、P 加点
        elif x == 's':
            r, s, p = max(s, p) + R, max(p, r), max(r, s)
        elif x == 'p':
            r, s, p = max(s, p), max(p, r) + S, max(r, s)

    return max(r, s, p)


answer = sum(solve(t) for t in Ts)
print(answer)