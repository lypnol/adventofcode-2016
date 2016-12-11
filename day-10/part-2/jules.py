from submission import Submission

class JulesSubmission(Submission):

    def author(self):
        return 'Jules'

    def run(self, s):

        outputsToCheck = (0,1,2)
        resultat = 1
        
        class Bot:

            def __init__(self,id):
                self.lower = None
                self.upper = None
                self.lowerOutput = None
                self.upperOutput = None
                self.value = []
                self.id = id

            def addValue(self,value):
                self.value.append(value)
                result = [1,1]
                if len(self.value) == 2:
                    if self.lower != None:
                        inter = self.lower.addValue(min(self.value))
                        result = (result[0]*inter[0],result[1]*inter[1])
                    elif self.lowerOutput in outputsToCheck:
                        result[0] = min(self.value)
                    if self.upper != None:
                        inter = self.upper.addValue(max(self.value))
                        result = (result[0]*inter[0],result[1]*inter[1])
                    elif self.upperOutput in outputsToCheck:
                        result[1] = max(self.value)
                    self.value = []
                return result

            def setLower(self,lower):
                self.lower = lower

            def setUpper(self,upper):
                self.upper = upper

            def setLowOutput(self,out):
                self.lowerOutput = out

            def setUpperOutput(self,out):
                self.upperOutput = out


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
                else:
                    bots[nb].setLowOutput(low)
                if data[10] != "output":
                    bots[nb].setUpper(bots[up])
                else:

                    bots[nb].setUpperOutput(up)
            elif data[0] == "value":
                val = int(data[1])
                nb = int(data[5])
                toDo.append((nb,val))

        for nb,val in toDo:
            result = bots[nb].addValue(val)
            resultat = resultat*result[0]*result[1]

        return resultat

