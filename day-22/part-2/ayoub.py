from submission import Submission
from copy import deepcopy
from heapq import *


class AyoubSubmission(Submission):
    states = {}

    def author(self):
        return 'Ayoub'

    def run(self, s):
        s = s.rstrip().split('\n')[2:]

        class State(object):

            @staticmethod
            def hash(m, pos, e):
                return hash(' '.join([str(e), str(pos)]))

            def __init__(self, m, pos, empty=None):
                self.m = deepcopy(m)
                self.pos = pos
                self.parent = None
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
                self._h = State.hash(self.m, self.pos, self.e)
                return self._h

            def __eq__(self, o):
                return isinstance(o, State) and hash(o) == self.__hash__()

            def __str__(self):
                m = deepcopy(self.m)
                for i in range(len(m)):
                    for j in range(len(m[i])):
                        if (i,j) == self.pos:
                            m[i][j] = 'G'
                        elif (i,j) == self.e:
                            m[i][j] = '_'
                        elif m[i][j][0] > 100:
                            m[i][j] = '#'
                        else:
                            m[i][j] = '.'
                return '\n'.join([' '.join(map(str, m[i])) for i in range(len(m))])

            def __repr__(self):
                return self.__str__()

            def next_states(self):
                m = self.m
                pos = self.pos
                n = []
                e = self.e

                moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                for u, v in moves:
                    x, y = e  # empty spot
                    i, j = x + u, y + v
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
                de = (self.pos[0] - self.e[0] - 1), (self.pos[1] - self.e[1])
                return (de[0]**2 + de[1]**2)**0.5

        def display(state):
            print "\033[0;0f" + "\n".join([' '.join([' ' for _ in range(500)]) for i in range(20)])
            print "\033[0;0f" + str(state)

        def new_state(m, p, e=None):
            h = State.hash(m, p, e)
            if h in self.states:
                return self.states[h]
            s = State(m, p, e)
            self.states[hash(s)] = s
            return s

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
            if current.e[0] == current.pos[0]-1 and current.e[1] == current.pos[1]:
                return current.G + (len(current.m)-2)*5 + 1
            if current.pos == (0, 0):
                return current.G
            closedset.add(hash(current))
            for n in current.next_states():
                if n.G > current.G + 1 and hash(n) not in closedset:
                    n.G = current.G + 1
                    for i, (_, s) in enumerate(openset):
                        if hash(s) == hash(n):
                            openset.pop(i)
                            heapify(openset)
                            break
                    heappush(openset, (n.G + n.heuristic(), n))
                    n.parent = current

        return None
