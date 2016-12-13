from submission import Submission
from itertools import combinations
from copy import deepcopy
from time import sleep
from heapq import *

WIDTH = 15
elements = {}
states_cache = {}

def gen_primes():
    """
    Generate an infinite sequence of prime numbers.
    """
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1
primes_generator = gen_primes()


class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        global elements, states_cache

        elements = {}
        states_cache = {}


        class State(object):

            @staticmethod
            def hash(pos, floors):
                global elements
                h = [str(pos)]
                for i in range(4):
                    floor_hash = 1
                    for j in range(WIDTH):
                        if floors[i][j] != ' ':
                            floor_hash *= elements[floors[i][j]]
                    h.append(str(floor_hash))
                return hash(' '.join(h))

            @staticmethod
            def is_safe_move(elements, last, row):
                if len(elements) == 0: return True
                last = [x for x in last if x not in elements]
                row.extend(elements)

                for e in row:
                    if e[-1] == 'M':
                        for g in row:
                            if g[-1] == 'G' and str(g[:-1] + 'M') not in row:
                                return False

                for e in last:
                    if e[-1] == 'M':
                        for g in last:
                            if g[-1] == 'G' and str(g[:-1] + 'M') not in last:
                                return False

                return True

            @staticmethod
            def check_safe(rows):
                for elements in rows:
                    M = [x[:-1] for x in elements if x[-1] == 'M']
                    G = [x[:-1] for x in elements if x[-1] == 'G']
                    if G:
                        for m in M:
                            if m not in G:
                                return False
                return True

            @staticmethod
            def is_stupid_move(comb, u):
                if len(comb) == 2:
                    if u < 0 and comb[0][:-1] == comb[1][:-1] and comb[0][-1] != comb[1][-1]:
                        return True
                    if comb[0][-1] == comb[1][-1] and comb[0][-1] == 'G':
                        return True
                elif len(comb) == 1 and comb[0][-1] == 'G':
                    return True
                return False

            @staticmethod
            def move(floors, pos, dist, elements):
                for e in elements:
                    idx = floors[pos].index(e)
                    for i in range(WIDTH):
                        if floors[pos+dist][i] == ' ':
                            floors[pos+dist][i] = e
                            floors[pos][idx] = ' '
                            break
                return floors


            def __init__(self, pos, floors):
                global primes_generator, states_cache
                self.hash = State.hash(pos, floors)
                self.pos = pos
                self.floors = deepcopy(floors)
                self.next = []
                self.heur = None
                self.parent = None
                self.G = float('inf')

            def __hash__(self):
                return self.hash

            def __eq__(self, o):
                return isinstance(o, State) and o.hash == self.hash

            def __str__(self):
                return "\n".join(
                    [('.   ' if self.pos!=i else 'E   ' ) +\
                      ' '.join(self.floors[i]) for i in range(3, -1, -1) ])

            def __repr__(self):
                return self.__str__()


            def next_states(self):
                if self.next:
                    return self.next

                self.next = []
                current_components = [x for x in self.floors[self.pos] if x!=' ']
                all_possible = []

                if len(current_components) == 0:
                    return []
                if len(current_components) >= 1:
                    for comb in current_components:
                        all_possible.append((comb,))
                if len(current_components) >= 2:
                    for comb in combinations(current_components, 2):
                        all_possible.append(comb)

                moves = []
                if self.pos < 3: moves.extend([u for u in range(1, 4-self.pos)])
                if self.pos > 0: moves.extend([-u for u in range(1, self.pos+1)])

                for u in moves:
                    next_pos = self.pos + u
                    for comb in all_possible:
                        if State.is_stupid_move(comb, u):
                            continue

                        if State.check_safe([[x for x in self.floors[self.pos] if x not in list(comb) and x!=' ']]) and \
                           State.check_safe([[x for x in self.floors[i] if x!=' '] + list(comb) for i in range(min(self.pos+1, next_pos+1), max(self.pos+1, next_pos+1), u//abs(u))]):
                            floors = State.move(deepcopy(self.floors), self.pos, u, comb)
                            self.next.append((abs(u), newState(next_pos, floors)))

                return self.next

            def heuristic(self):
                if self.heur is not None:
                    return self.heur
                val = 0
                for i in range(3):
                    for j in range(WIDTH):
                        if self.floors[i][j] != ' ':
                            val += 3 - i
                self.heur = val
                return self.heur

        def newState(pos, floors):
            global states_cache
            h = State.hash(pos, floors)
            if h in states_cache:
                return states_cache[h]
            else:
                states_cache[h] = State(pos, floors)
            return states_cache[h]


        def display(state):
            print "\033[0;0f" + "\n".join([' '.join([' ' for _ in range(500)]) for i in range(20)])
            print "\033[0;0f" + str(state)


        floors = [[' ' for _ in range(WIDTH)] for n in range(4)]
        for i, line in enumerate(s.rstrip().split('\n')[:-1]):
            line = line.replace(', and a ', ' a ', 5)
            line = line.replace(' and a ', ' a ', 5)
            line = line.replace(', a ', ' a ', 5)
            line = line.replace('.', '', 5)
            if i == 0:
                line += ' a elerium generator a elerium-compatible microchip a dilithium generator a dilithium-compatible microchip'
            for j, component in enumerate(line.split(' a ')[1:]):
                tokens = component.split()
                if tokens[1] == 'generator':
                    floors[i][j] = tokens[0] + 'G'
                else:
                    floors[i][j] = tokens[0].split('-')[0] + 'M'
                if floors[i][j] not in elements:
                    elements[floors[i][j]] = primes_generator.next()

        start = newState(0, floors)
        start.G = 0
        openset = [(start.G + start.heuristic(), start)]
        closedset = set()

        while openset:
            _, current = heappop(openset)
            if current.heuristic() == 0:
                return current.G
            closedset.add(current)
            for cost, state in current.next_states():
                if state in closedset:
                    continue
                if state.G > current.G + cost:
                    state.parent = current
                    state.G = current.G + cost
                    for i, (_, s) in enumerate(openset):
                        if hash(s) == hash(state):
                            openset.pop(i)
                            heapify(openset)
                            break
                    heappush(openset, (state.G + state.heuristic(), state))
        return None
