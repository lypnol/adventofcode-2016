from submission import Submission

class JulesSubmission(Submission):

    def author(self):
        return 'Jules'

    def run(self, s):
        registers = {'a':0,'b':0,'c':1,'d':0}
        lines = s.strip().split('\n')
        i = 0
        while i < len(lines):
            instructions = lines[i].split(' ')
            cmd = instructions[0]
            
            if cmd == "cpy":
                variable = instructions[2]
                value = instructions[1]
                if value in registers:
                    registers[variable] = registers[value]
                else:
                    registers[variable] = int(value)
            elif cmd == "inc":
                variable = instructions[1]
                #Variable Transfer pattern detection
                if i < len(lines)-2:
                    l1 = lines[i+1].split(' ')
                    l2 = lines[i+2].split(' ')
                    if l1[0] == "dec" and l2[0] == "jnz" and l2[1] == l1[1] and l2[2] == "-2":
                        registers[variable] += registers[l1[1]]
                        registers[l1[1]] = 0
                        i += 2
                        continue
                registers[variable] += 1
            elif cmd == "dec":
                variable = instructions[1]
                registers[variable] -= 1
            elif cmd == "jnz":
                variable = instructions[1]
                value = int(instructions[2])
                if (variable in registers and registers[variable] != 0) or (variable not in registers and int(variable) != 0):
                    i += value
                    continue
            i += 1

        return registers["a"]