from submission import Submission

class JulesSubmission(Submission):

    def author(self):
        return 'Jules'

    def run(self, s):
        #Wow, such difference between this and the first part ! :')
        import string

        length = len(s.split('\n')[0])
        frequencies = []
        ##INIT Frequencies array
        for i in range(length):
            frequencies.append([])
        for char in string.ascii_lowercase:
            for i in range(length):
                frequencies[i].append((char,0))
        ##END INIT

        for line in s.rstrip().split('\n'):
            for i in range(len(line.rstrip())):
                charOffset = string.ascii_lowercase.index(line[i])
                frequencies[i][charOffset] = (frequencies[i][charOffset][0],frequencies[i][charOffset][1]+1)

        sol = ""
        for i in range(length):
            sol += sorted(frequencies[i], key=lambda x: (x[1],x[0]))[0][0]

        return sol
