from submission import Submission

class JulesSubmission(Submission):

    def author(self):
        return 'Jules'

    def run(self, s):
        import re
        width = 50
        heigth = 6
        
        def shiftRow(table,a,b):
            import copy
            newTable = list(table[a])
            for i in range(width):
                table[a][i] = newTable[(i-b)%width]

        def shiftColumn(table,a,b):
            import copy
            newTable = []
            for i in range(heigth):
                newTable.append(table[i][a])
            for i in range(heigth):
                table[i][a] = newTable[(i-b)%heigth]

        def rect(table,a,b):
            for i in range(b):
                for j in range(a):
                    table[i][j] = "#"
            return table

        table =[["" for i in range(width)] for j in range(heigth)]

        for line in s.strip().split('\n'):
            action = line.split(' ')
            if action[0] == "rect":
                coordinates = action[1].split('x')
                rect(table,int(coordinates[0]),int(coordinates[1]))
            else:
                a = int(line.split('=')[1][:2].strip())
                b = int(line[-2:].strip())
                if action[1] == "row":
                    shiftRow(table,a,b)
                else:
                    shiftColumn(table,a,b)

        count = 0
        for i in range(heigth):
            for j in range(width):
                if table[i][j] == "#":
                    count += 1

        return count
