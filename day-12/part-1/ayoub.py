from submission import Submission


class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        s = s.rstrip()
        instructions = s.split('\n')
        reg = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
        i = 0
        while i < len(instructions) :
            t = instructions[i].split()
            if t[0] == 'cpy':
                if t[1] in reg:
                    reg[t[2]] = reg[t[1]]
                else:
                    reg[t[2]] = int(t[1])
            elif t[0] == 'inc':
                reg[t[1]] += 1
            elif t[0] == 'dec':
                reg[t[1]] -= 1
            elif t[0] == 'jnz':
                if (t[1] in reg and reg[t[1]] != 0) or \
                   (t[1] not in reg and int(t[1]) != 0):
                    i += int(t[2])
                    continue
            i += 1
        return reg['a']
