from submission import Submission

class JulesSubmission(Submission):

    def author(self):
        return 'Jules'

    def run(self, s):
        import hashlib

        salt = s.strip()
        password = [0]*8
        indexChanged = []
        index = 0
        while(len(indexChanged) < 8):
            md5 = hashlib.md5(salt + str(index)).hexdigest()
            if md5.startswith("00000"):
                position = int(md5[5],16)
                if position in range(0,8):
                    if not position in indexChanged:
                        password[position] = str(md5[6])
                        indexChanged.append(position)
            index += 1
        return "".join(password)

