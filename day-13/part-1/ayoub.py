from submission import Submission
from heapq import *


class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        s = s.rstrip()
        N = int(s)
        start = 1, 1
        goal = 31,39

        def is_wall(x, y):
            r = x*x + 3*x + 2*x*y + y + y*y
            r += N
            return bin(r).count("1") % 2 == 1

        def heuristic(x, y):
            a, b = goal
            return ((x - a)**2 + (y - b)**2)**0.5

        dist = {start: 0}
        openset = [(heuristic(*start), start)]
        closedset = set()
        while openset:
            _, (x, y) = heappop(openset)
            if x == goal[0] and y == goal[1]:
                return dist[(x, y)]
            closedset.add((x, y))
            for u,v in [(1,0), (0,1), (-1,0), (0, -1)]:
                node = (x+u, y+v)
                if x+u >= 0 and y+v >=0 and\
                 not is_wall(*node) and node not in closedset:
                    if node not in dist or dist[node] < dist[(x,y)] + 1:
                        dist[node] = dist[(x,y)] + 1
                        for i, n in enumerate(openset):
                            if n == node:
                                openset.pop(i)
                                heapify(openset)
                                break
                        heappush(openset, (dist[node] + heuristic(*node), node))

        return None
