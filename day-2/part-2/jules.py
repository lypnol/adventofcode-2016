from submission import Submission

class AyoubSubmission(Submission):

    def author(self):
        return 'Jules'

    def getElement(self,position):
		if position[1] == 2:
			return "1"
		elif position[1] == 1:
			return str(2+position[0]+1)
		elif position[1] == 0:
			return str(5+position[0]+2)
		elif position[1] == -1:
			return "ABC"[position[0]+1]
		elif position[1] == -2:
			return "D"

    def run(self, s):
		move = {"R" : (1,0), "L": (-1,0), "U" : (0,1), "D" : (0,-1)}
		current = (-2,0)
		positions = ""
		for line in s.rstrip().split('\n'):		
			for instruction in line.strip():
				newCurrent = (current[0]+move[instruction][0],current[1]+move[instruction][1])
				if abs(newCurrent[0]) + abs(newCurrent[1]) <= 2:
					current = newCurrent
			positions += self.getElement(current)
		return positions