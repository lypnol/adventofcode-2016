from submission import Submission

class JulesSubmission(Submission):

    def author(self):
        return 'Jules'

    def run(self, s):
        registers = {'a':12,'b':0,'c':0,'d':0}
        lines = s.strip().split('\n')
        i = 0
        toggled = []
        toggleInstruction = {"jnz":"cpy","inc":"dec","dec":"inc","cpy" : "jnz", "tgl" : "inc"}
        while i < len(lines):
            instructions = lines[i].split(' ')
            cmd = instructions[0]
            if i in toggled:
                for _ in range(toggled.count(i)):
                    cmd = toggleInstruction[cmd]
            if cmd == "tgl":
                nb = instructions[1]
                if nb in registers:
                    nb = registers[nb]
                toggled.append(nb+i)
            elif cmd == "cpy":
                variable = instructions[2]
                value = instructions[1]
                if value in registers:
                    registers[variable] = registers[value]
                elif variable in registers:
                    registers[variable] = int(value)
            elif cmd == "inc":
                variable = instructions[1]
                #Variable Transfer pattern detection
                if i < len(lines)-5:
                    l = [lines[i+j].split(' ') for j in range(1,5)]
                    if l[0][0] == "dec" and l[1][0] == "jnz" and l[1][2] == "-2" and l[2][0] == "dec" and l[3][0] == "jnz" and l[3][2] == "-5":
                        registers[variable] += registers[l[0][1]]*registers[l[2][1]]
                        registers[l[0][1]] = 0
                        registers[l[2][1]] = 0
                        i += 5
                        continue
                if i < len(lines)-3:
                    l1 = lines[i+1].split(' ')
                    l2 = lines[i+2].split(' ')
                    if l1[0] == "dec" and l2[0] == "jnz" and l2[1] == l1[1] and l2[2] == "-2":
                        registers[variable] += registers[l1[1]]
                        registers[l1[1]] = 0
                        i += 3
                        continue
                registers[variable] += 1
            elif cmd == "dec":
                variable = instructions[1]
                registers[variable] -= 1
            elif cmd == "jnz":
                variable = instructions[1]
                if instructions[2] in registers:
                    value = registers[instructions[2]]
                else:
                    value = int(instructions[2])
                if (variable in registers and registers[variable] != 0) or (variable not in registers and int(variable) != 0):
                    i += value
                    continue
            i += 1

        return registers["a"]