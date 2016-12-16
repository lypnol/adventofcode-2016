from submission import Submission

class JulesSubmission(Submission):

    def author(self):
        return 'Jules'

    def run(self, s):

        puzzle = s.strip()
        length = 272

        def expandElement(puzzle):
            return puzzle+"0"+(puzzle[::-1].replace("0","2").replace("1","0").replace("2","1"))

        def checksum(puzzle):
            check = puzzle
            while True:
                newCheck = ""
                for i in range(0,len(check),2):
                    if check[i:i+2] == "00" or check[i:i+2] == "11":
                        newCheck += "1"
                    else:
                        newCheck += "0"
                check = newCheck
                if len(check) % 2 == 1:
                    break
            return check

        expanded = expandElement(puzzle)
        while len(expanded)<length:
            expanded = expandElement(expanded)
        return checksum(expanded[:length])
