from submission import Submission
import md5


class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, salt):
        salt = salt.rstrip()

        N = 64

        def has_five(s):
            fives = set()
            for i in range(len(s)-4):
                if s[i] == s[i+1] and s[i] == s[i+2] \
                and s[i] == s[i+3] and s[i] == s[i+4]:
                    fives.add(s[i])
            return fives

        def has_triple(s):
            for i in range(len(s)-2):
                if s[i] == s[i+1] and s[i] == s[i+2]:
                    return s[i]
            return None

        i = 0
        looking_for = []
        found = 0
        while True:
            to_delete = []
            for j, (idx, x) in enumerate(looking_for):
                if i - idx >= 1000:
                    to_delete.append(j)
            for j in to_delete[::-1]:
                del looking_for[j]

            Hash = md5.new(salt + str(i)).hexdigest()
            fives = has_five(Hash)
            for f in fives:
                to_delete = []
                for j, (idx, t) in enumerate(looking_for):
                    if i - idx < 1000 and t == f:
                        to_delete.append(j)
                        found += 1
                        if found == N:
                            return idx
                for j in to_delete[::-1]:
                    del looking_for[j]

            t = has_triple(Hash)
            if t is not None:
                looking_for.append((i, t))

            i += 1

        return
