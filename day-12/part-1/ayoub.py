from submission import Submission


class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        s = s.rstrip()

        def find_pattern_1(i1, i2, i3):
            '''
            Look for patterns:
                inc x
                dec y
                jnz y -2
            which translate to:
                x += y
                y = 0
            '''
            t1 = i1.split()
            t2 = i2.split()
            t3 = i3.split()
            if t1[0] == 'inc' and t2[0] == 'dec' and t3[0] == 'jnz' and\
               t3[2] == '-2' and t3[1] == t2[1]:
               return True
            return False

        def find_pattern_2(i1, i2):
            '''
            Look for patterns:
                dec x
                jnz x -1
            which translate to:
                x = 0
            '''
            t1 = i1.split()
            t2 = i2.split()
            if t1[0] == 'dec' and t2[0] == 'jnz' and t2[2] == '-1' \
            and t1[1] == t2[1]:
               return True
            return False

        def find_pattern_3(i1, i2, i3):
            '''
            Look for patterns:
                dec x
                inc y
                jnz x -2
            which translate to:
                y += x
                x = 0
            '''
            t1 = i1.split()
            t2 = i2.split()
            t3 = i3.split()
            if t1[0] == 'dec' and t2[0] == 'inc' and t3[0] == 'jnz' and\
               t3[2] == '-2' and t3[1] == t1[1]:
               return True
            return False

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
                if i < len(instructions) - 2 and find_pattern_1(*instructions[i:i+3]):
                    t1 = instructions[i].split()
                    t2 = instructions[i+1].split()
                    reg[t1[1]] += reg[t2[1]]
                    reg[t2[1]] = 0
                    i += 3
                    continue
                else:
                    reg[t[1]] += 1
            elif t[0] == 'dec':
                if i < len(instructions) - 2 and find_pattern_3(*instructions[i:i+3]):
                    t1 = instructions[i].split()
                    t2 = instructions[i+1].split()
                    reg[t2[1]] += reg[t1[1]]
                    reg[t1[1]] = 0
                    i += 3
                    continue
                elif i < len(instructions) - 1 and find_pattern_2(*instructions[i:i+2]):
                    t1 = instructions[i].split()
                    reg[t1[1]] = 0
                    i += 2
                    continue
                reg[t[1]] -= 1
            elif t[0] == 'jnz':
                if (t[1] in reg and reg[t[1]] != 0) or \
                   (t[1] not in reg and int(t[1]) != 0):
                    i += int(t[2])
                    continue
            i += 1
        return reg['a']
