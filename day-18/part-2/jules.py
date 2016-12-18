from submission import Submission

class JulesSubmission(Submission):

    def author(self):
        return 'Jules'

    def run(self, s):

        def is_safe_tile(a,b,c):
            if a == '^' and b == '^' and c == '.':
                return False
            elif a == '.' and b == '^' and c == '^':
                return False
            elif a == '^' and b == '.' and c == '.':
                return False
            elif a == '.' and b == '.' and c == '^':
                return False
            return True

        row = s.strip()
        rowNumber = 400000
        nbSafeTile = 0
        visitedRow = [row]
        for i in range(rowNumber):
            newRow = ""
            for index in range(len(row)):
                if row[index] == '.':
                    nbSafeTile += 1
                newRow += '.' if is_safe_tile(row[index-1] if index > 0 else '.',row[index],row[index+1] if index < len(row) - 1 else '.') else '^'
            row = newRow

        return nbSafeTile

