from submission import Submission

class JulesSubmission(Submission):

    def author(self):
        return 'Jules'

    def run(self, s):

        def stretchedHash(salt,index):
            md5 = salt+str(index)
            for _ in range(2017):
                md5 = hashlib.md5(md5).hexdigest().lower()
            return md5

        import hashlib
        import string

        salt = s.strip()
        key = ""
        keyNbr = 0
        index = 0
        hashesArray = []
        for i in range(1000):
            hashesArray.append(stretchedHash(salt, i))
        while(keyNbr < 64):
            newMd5 = stretchedHash(salt,index+1000)
            hashesArray.append(newMd5)
            md5 = hashesArray.pop(0)
            numberFound = -1
            nbrIndex = len(md5)
            for nbr in string.digits+"abcdef":
                try:
                    place = md5.index(str(nbr)*3)
                    if place < nbrIndex :
                        numberFound = nbr
                        nbrIndex = place
                except:
                    0
            if numberFound != -1:
                for el in hashesArray:
                    if str(numberFound)*5 in el:
                        keyNbr += 1
                        break
            index += 1
        return index-1