
move = {"R" : (1,0), "L": (-1,0), "U" : (0,1), "D" : (0,-1)}

def solve(puzzle):
	current = (1,1)
	sol = ""
	for line in puzzle:
		for instruction in line.strip():
			new = (current[0]+move[instruction][0],current[1]+move[instruction][1])
			current = (new[0] if new[0] in range(0,3) else current[0] , new[1] if new[1] in range(0,3) else current[1])
		sol += str(1+current[0]+(2-current[1])*3)
	return sol

def getElement(position):
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

def solve2(puzzle):
	current = (-2,0)
	positions = ""
	for line in puzzle:		
		for instruction in line.strip():
			newCurrent = (current[0]+move[instruction][0],current[1]+move[instruction][1])
			if abs(newCurrent[0]) + abs(newCurrent[1]) <= 2:
				current = newCurrent
		positions += getElement(current)
	return positions


file = open('input.txt','r+')
puzzle = file.readlines()
print "~Part 1~"
print solve(puzzle)
print ""
print "~Part 2~"
print solve2(puzzle)
