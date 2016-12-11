from submission import Submission

class JulesSubmission(Submission):

    def author(self):
        return 'Jules'

    def run(self, s):

        toSearch = (17,61)
        
        class Bot:

            def __init__(self,id):
                self.lower = None
                self.upper = None
                self.value = []
                self.id = id

            def addValue(self,value):
                self.value.append(value)
                # print len(self.value)
                if toSearch[0] in self.value and toSearch[1] in self.value:
                    return self.id
                if len(self.value) == 2:
                    a,b = (0,0)
                    if self.lower != None:
                        a = self.lower.addValue(min(self.value))
                    if self.upper != None:
                        b = self.upper.addValue(max(self.value))
                    self.value = []
                    return max(a,b)
                return 0

            def setLower(self,lower):
                self.lower = lower

            def setUpper(self,upper):
                self.upper = upper


        nbLines = len(s.strip().split('\n'))
        toDo = []
        bots = [ Bot(i) for i in range(nbLines)]
        for line in s.strip().split('\n'):
            data = line.split(' ')
            if data[0] == "bot":
                nb = int(data[1])
                low = int(data[6])
                up = int(data[11])
                if data[5] != "output":
                    bots[nb].setLower(bots[low])
                if data[10] != "output":
                    bots[nb].setUpper(bots[up])
            elif data[0] == "value":
                val = int(data[1])
                nb = int(data[5])
                toDo.append((nb,val))

        for nb,val in toDo:
            result = bots[nb].addValue(val)
            if result != 0:
                return result

