from submission import Submission

class AyoubSubmission(Submission):

    def author(self):
        return 'Jules'

    def run(self, s):
		move = {"R" : (1,0), "L": (-1,0), "U" : (0,1), "D" : (0,-1)}
		current = (1,1)
		sol = ""
		for line in s.rstrip().split('\n'):
			for instruction in line.strip():
				new = (current[0]+move[instruction][0],current[1]+move[instruction][1])
				current = (new[0] if new[0] in range(0,3) else current[0] , new[1] if new[1] in range(0,3) else current[1])
			sol += str(1+current[0]+(2-current[1])*3)
		return sol
	