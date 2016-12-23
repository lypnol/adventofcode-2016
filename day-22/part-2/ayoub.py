from submission import Submission
from copy import deepcopy


class AyoubSubmission(Submission):
    states = {}

    def author(self):
        return 'Ayoub'

    def run(self, s):
        s = s.rstrip().split('\n')[2:]

        class State(object):

            @staticmethod
            def hash(m, pos):
                s = []
                for i in range(len(m)):
                    s.append(' '.join(map(str, m[i])))

                return hash(' '.join(s) + ' ' +str(pos))

            def __init__(self, m, pos):
                self.m = deepcopy(m)
                self.pos = pos
                self._h = None

            def __hash__(self):
                if self._h is not None:
                    return self._h
                self._h = State.hash(self.m, self.pos)
                return self._h

            def __eq__(self, o):
                return isinstance(o, State) and hash(o) == self.__hash__()

            def next_states(self):


                return []

        def new_state(m, p):
            h = State.hash(m, p)
            if h in self.states:
                return self.states[h]
            return self.states[h] = State(m, p)

        nodes = []
        i = -1
        for line in s:
            tokens = line.split()
            name = tokens[0].split('-')
            if int(name[1][1:]) > i:
                i += 1
                nodes.append([])

            nodes[i].append((int(tokens[2][:-1]), int(tokens[3][:-1])))

        states = set()
        states.add(State(nodes))
