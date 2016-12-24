from submission import Submission
from heapq import *
from copy import deepcopy
from collections import defaultdict

class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        """###########
#0.1.....2#
#.#######.#
#4.......3#
###########
"""
        s = s.rstrip()
        g = []
        for line in s.split('\n'):
            g.append(list(line))

        def shortest_paths(g, start):
            Q = [(0, start)]
            D = {start: 0}
            S = defaultdict(list)
            P = {}
            V = set()
            while Q:
                _, (i, j) = heappop(Q)
                if g[i][j] not in ['#', '.']:
                    x, y = i, j
                    found = False
                    while (x, y) in P:
                        if g[x][y] not in ['#', '.']\
                        and (x, y) != start:
                            S[int(g[i][j])].append((int(g[x][y]), D[(x, y)]))
                        x, y = P[(x, y)]
                V.add((i, j))
                for u, v in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    x, y = i + u, j + v
                    if x >= 0 and x < len(g) and y >=0 and y < len(g[x])\
                    and g[x][y] != '#' and (x, y) not in V:
                        if (x, y) not in D or D[(x, y)] > D[(i, j)] + 1:
                            D[(x, y)] = D[(i, j)] + 1
                            for k, (_, (a, b)) in enumerate(Q):
                                if (a, b) == (x, y):
                                    Q.pop(k)
                                    heapify(Q)
                                    break
                            P[(x, y)] = i, j
                            heappush(Q, (D[(x, y)], (x, y)))
            for u in S:
                S[u].reverse()
            return S

        graph = {}
        numbers = set()
        for i in range(len(g)):
            for j in range(len(g[i])):
                if g[i][j] not in ['#', '.']:
                    graph[int(g[i][j])] = shortest_paths(g, (i, j))
                    numbers.add(int(g[i][j]))

        def explore(graph, numbers, n=0, visited=[]):
            V = deepcopy(visited) + [n]
            if set(V) == numbers:
                return sum([graph[V[i]][V[i+1]][-1][1] for i in range(len(V)-1)]) +\
                graph[V[-1]][0][-1][1]

            min_p = float("inf")
            for u in numbers:
                if u not in V:
                    path = graph[n][u]
                    for v, d in path[:-1]:
                        V.append(v)
                    p = explore(graph, numbers, u, V)
                    if p < min_p:
                        min_p = p

            return min_p

        return explore(graph, numbers)
