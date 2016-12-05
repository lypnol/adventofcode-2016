from submission import Submission

class JulesSubmission(Submission):

    def author(self):
        return 'Jules'

    def run(self, s):
        import hashlib

        salt = s.strip()
        password = ""
        index = 0
        while(len(password) != 8):
            md5 = hashlib.md5(salt + str(index)).hexdigest()
            if md5.startswith("00000"):
                password += md5[5]
            index += 1
        return password