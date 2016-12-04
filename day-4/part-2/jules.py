from submission import Submission

class JulesSubmission(Submission):

    def author(self):
        return 'Jules'

    def unCipher(self,s,id):
        import string
        charset = string.ascii_lowercase
        wanted = "northpole object storage" #I had to run code once to know what was the wanted string. This change is for computation time purposes. For the first run I searched "north" and "pole" in the newLine
        newLine = ""
        for word in s:
            for c in word:
                newLine += charset[(charset.index(c)+int(id))%len(charset)]
                if newLine != wanted[:len(newLine)]:
                    return False
            newLine += " "
        return True

    def run(self, s):

        for line in s.rstrip().split('\n'):
            elements = line.split('-')
            id = elements[-1].split('[')[0]

            newLine = self.unCipher(elements[:-1],id)
            if newLine != False:
                return int(id)
