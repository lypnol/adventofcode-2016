from submission import Submission
from copy import deepcopy
from heapq import *


class AyoubSubmission(Submission):
    states = {}

    def author(self):
        return 'Ayoub'

    def run(self, s):

        """
Filesystem            Size  Used  Avail  Use%
/dev/grid/node-x0-y0   10T    8T     2T   80%
/dev/grid/node-x0-y1   11T    6T     5T   54%
/dev/grid/node-x0-y2   32T   28T     4T   87%
/dev/grid/node-x1-y0    9T    7T     2T   77%
/dev/grid/node-x1-y1    8T    0T     8T    0%
/dev/grid/node-x1-y2   11T    7T     4T   63%
/dev/grid/node-x2-y0   10T    6T     4T   60%
/dev/grid/node-x2-y1    9T    8T     1T   88%
/dev/grid/node-x2-y2    9T    6T     3T   66%
"""
        s = s.rstrip().split('\n')[2:]

        class State(object):

            @staticmethod
            def hash(m, pos):
                s = []
                for i in range(len(m)):
                    s.append(' '.join(map(str, m[i])))

                return hash(' '.join(s) + ' ' +str(pos))

            def __init__(self, m, pos, empty=None):
                self.m = deepcopy(m)
                self.pos = pos
                self._h = None
                self.G = float("inf")
                self.e = empty
                if self.e is None:
                    for i in range(len(m)):
                        for j in range(len(m[i])):
                            if m[i][j][0] == 0:
                                self.e = i, j
                                break
                        if self.e is not None:
                            break

            def __hash__(self):
                if self._h is not None:
                    return self._h
                self._h = State.hash(self.m, self.pos)
                return self._h

            def __eq__(self, o):
                return isinstance(o, State) and hash(o) == self.__hash__()

            def __str__(self):
                m = self.m
                return '\n'.join([' '.join(map(str, m[i])) for i in range(len(m))])+\
                       '\n' + str(self.pos)

            def __repr__(self):
                return self.__str__()

            def next_states(self):
                m = self.m
                pos = self.pos
                n = []
                e = self.e

                moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                for u, v in moves:
                    x, y = e
                    i, j = x + u, y + v
                    useful = True
                    if u > 0 and pos[0] - e[0] < 0:
                        if pos[1] == e[1]:
                            if m[x][y][1] >= m[x][y][0]

                    if i >= 0 and i < len(m) and j >= 0 and j < len(m[i])\
                    and m[x][y][1] >= m[i][j][0]:
                        c = deepcopy(m)
                        c[x][y] = (m[x][y][0] + m[i][j][0], m[x][y][1] - m[i][j][0])
                        c[i][j] = (0, m[i][j][1] + m[i][j][0])
                        cp = pos
                        if i == pos[0] and j == pos[1]:
                            cp = (x, y)
                        ce = i, j
                        n.append(new_state(c, cp, e=ce))

                return n

            def heuristic(self):
                d = abs(self.pos[0]) + abs(self.pos[1])
                return d

        def display(state):
            print "\033[0;0f" + "\n".join([' '.join([' ' for _ in range(500)]) for i in range(20)])
            print "\033[0;0f" + str(state)

        def new_state(m, p, e=None):
            h = State.hash(m, p)
            if h in self.states:
                return self.states[h]
            self.states[h] = State(m, p, e)
            return self.states[h]

        m = []
        i = -1
        for line in s:
            tokens = line.split()
            name = tokens[0].split('-')
            if int(name[1][1:]) > i:
                i += 1
                m.append([])
            m[i].append((int(tokens[2][:-1]), int(tokens[3][:-1])))

        start = new_state(m, (len(m)-1, 0))
        start.G = 0
        openset = [(0, start)]
        closedset = set()

        while openset:
            _, current = heappop(openset)
            if current.heuristic() == 0:
                return current.G
            closedset.add(current)
            for n in current.next_states():
                if n.G > current.G + 1 and n not in closedset:
                    n.G = current.G + 1
                    for i, (_, s) in enumerate(openset):
                        if hash(s) == hash(n):
                            openset.pop(i)
                            heapify(openset)
                            break
                    heappush(openset, (n.G + n.heuristic(), n))

        return None
