from submission import Submission
from itertools import combinations
from copy import deepcopy
from time import sleep
import heapq

WIDTH = 15
hashes = {}

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
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

def hash_state(pos, floors):
    global hashes
    h = [str(pos)]
    for i in range(4):
        floor_hash = 1
        for j in range(WIDTH):
            if floors[i][j] != '.':
                floor_hash *= hashes[floors[i][j]]
        h.append(str(floor_hash))
    return ' '.join(h)

def already_been_here(pos, floors, past):
    return hash_state(pos, floors) in past

def is_safe_move(chips, f):
    if len(chips) == 0:
        return True
    for ch in f:
        if ch != '.' and ch[-1] == 'G' \
        and str(ch[:-1]+'M') not in f and str(ch[:-1]+'M') not in chips:
            return False
    return True

def move(state, pos, u, comb):
    for c in comb:
        idx = state[pos].index(c)
        for i in range(WIDTH):
            if state[pos+u][i] == '.':
                state[pos+u][i] = c
                state[pos][idx] = '.'
    return state

def next_states(pos, floors, past):
    states = []
    current_components = [x for x in floors[pos] if x!='.']
    all_possible = []

    if len(current_components) >= 1:
        for comb in current_components:
            all_possible.append((comb,))
    if len(current_components) >= 2:
        for comb in combinations(current_components, 2):
            all_possible.append(comb)
    all_possible.append(tuple())

    moves = []
    if pos < 3: moves.extend([u for u in range(1, 4-pos)])
    if pos > 0: moves.extend([-u for u in range(1, pos+1)])

    for u in moves:
        next_pos = pos + u
        for comb in all_possible:
            if is_safe_move(list(comb), floors[next_pos]):
                new_state = move(deepcopy(floors), pos, u, comb)
                if not already_been_here(next_pos, new_state, past):
                    states.append((next_pos, new_state))

    return states

def is_done(floors):
    for f in floors[:-1]:
        for x in f:
            if x != '.':
                return False
    return True

def show(floors, pos):
    print "\033[5;0f" + "\n".join([' '.join([' ' for _ in range(WIDTH+100)]) for i in range(10)])
    print "\033[5;0f" + "\n".join([('.   ' if pos!=i else 'E   ' ) + ' '.join(floors[i]) for i in range(3, -1, -1)])

class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        s = s.rstrip()
        global hashes
        hashes = {}
        primes_generator = gen_primes()

        floors = [['.' for _ in range(WIDTH)] for n in range(4)]
        for i, line in enumerate(s.split('\n')[:-1]):
            line = line.replace(', and a ', ' a ', 5)
            line = line.replace(' and a ', ' a ', 5)
            line = line.replace(', a ', ' a ', 5)
            for j, component in enumerate(line.split(' a ')[1:]):
                tokens = component.split()
                if tokens[1] == 'generator':
                    floors[i][j] = tokens[0] + 'G'
                else:
                    floors[i][j] = tokens[0].split('-')[0] + 'M'
                if floors[i][j] not in hashes:
                    hashes[floors[i][j]] = primes_generator.next()

        pos = 0

        dist = dict()
        dist[hash_state(0, deepcopy(floors))] = 0
        past = []
        Q = [(0, (0, deepcopy(floors)))]
        while Q:
            _, (pos, state) = heapq.heappop(Q)
            if is_done(state):
                return dist[hash_state(pos, state)]
            past.append(hash_state(pos, state))
            for next_pos, next_state in next_states(pos, state, past):
                d = abs(next_pos - pos)
                if hash_state(next_pos, next_state) not in dist or \
                   dist[hash_state(next_pos, next_state)] > dist[hash_state(pos, state)] + d:
                    dist[hash_state(next_pos, next_state)] = dist[hash_state(pos, state)] + d
                    for i, (_, (p, s)) in enumerate(Q):
                        if hash_state(p, s) == hash_state(next_pos, next_state):
                            Q.pop(i)
                            heapq.heapify(Q)
                            break
                    heapq.heappush(Q, (dist[hash_state(next_pos, next_state)], (next_pos, next_state)))

        return None
