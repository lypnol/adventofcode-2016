from submission import Submission

class CocoDay12Part1(Submission):

    register = {'a':0, 'b':0, 'c':1, 'd':0}

    def author(self):
        return "coco"

    def run(self, instructions):
        lines =  instructions.strip().split("\n")
        i = 0
        while i < len(lines):
            l = lines[i]
            elts = l.split()
            if elts[0] == "cpy":
                x, y = elts[1], elts[2]
                if x in self.register:
                    self.register[y] = self.register[x]
                else:
                    self.register[y] = int(x)
            elif elts[0] == "inc":
                if i < len(lines) - 2:
                    elts_1 = lines[i+1].split()
                    elts_2 = lines[i+2].split()
                    if elts_1[0] == "dec" and elts_2[0] == "jnz":
                        if elts_1[1] == elts_2[1]:
                            if elts_2[2] == '-2':
                                self.register[elts[1]] += self.register[elts_1[1]]
                                self.register[elts_1[1]] = 0
                                i += 2
                                continue
                x = elts[1]
                self.register[x] += 1
            elif elts[0] == "dec":
                self.register[elts[1]] -= 1
            else:
                x, y = elts[1], elts[2]
                if x in self.register:
                    if self.register[x] != 0:
                        i += int(y) - 1
                else:
                    if int(x) != 0:
                        i += int(y) - 1
            i += 1
        return self.register['a']
