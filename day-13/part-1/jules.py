from submission import Submission

class JulesSubmission(Submission):

    def author(self):
        return 'Jules'

    def run(self, s):

        inputNb = s.strip()

        def isOpen(node):
            result = node[0]*node[0] + 3*node[0] + 2*node[0]*node[1] + node[1] + node[1]*node[1] + int(inputNb)
            if bin(result).count("1") % 2 == 0:
                return True
            else:
                return False

        visited = {(1, 1)}
        steps = 0
        nextPlaces = visited

        while True:
            WhereIam = nextPlaces.copy()
            nextPlaces = set()
            dirs = [[-1,0],[1,0],[0,-1],[0,1]]
            for x, y in WhereIam:
                for nextX, nextY in [(x+dir[0],y+dir[1]) for dir in dirs]:
                    if nextX < 0 or nextY < 0 or (nextX, nextY) in visited or not isOpen((nextX, nextY)):
                        continue
                    visited.add((nextX, nextY))
                    nextPlaces.add((nextX, nextY))
            steps += 1
            if (31,39) in visited:
                return steps
