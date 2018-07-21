from collections import deque


def bfs(G, s):
    P, Q = {s:None}, deque([s])
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v in P: continue
            P[v] = u
            Q.append(v)
    return P


def main():
    a, b, c, d, e, f, g, h = range(8)
    g = [[b, c, d, e, f], [c, e], [d], [e], [f], [g, h], [f, h], [f, g]]
    print(bfs(g, a))


if __name__ == '__main__':
    main()