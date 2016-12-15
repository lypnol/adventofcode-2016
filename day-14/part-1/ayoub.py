from submission import Submission
import hashlib
import string


class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, salt):
        salt = salt.rstrip()

        N = 64

        def has_five(s):
            fives = set()
            for c in string.digits+"abcdef":
                if c*5 in s:
                    fives.add(c)
            return fives

        def has_triple(s):
            for i in range(len(s) - 2):
                if s[i] == s[i+1] and s[i+2] == s[i]:
                    return s[i]
            return ' '

        hashes_with_fives = []
        for i in range(1, 1001):
            h = hashlib.md5(salt + str(i)).hexdigest()
            fives = has_five(h)
            if fives: hashes_with_fives.append((i, fives))

        i = 0
        keys = 0
        while True:
            h = hashlib.md5(salt + str(i)).hexdigest()
            if has_triple(h) != ' ':
                is_key = False
                for idx, l in hashes_with_fives:
                    for c in l:
                        if c == has_triple(h):
                            keys += 1
                            if keys == N:
                                return i
                            is_key = True
                            break
                    if is_key: break

            to_remove = []
            for j, (idx, _) in enumerate(hashes_with_fives):
                if idx <= i+1:
                    to_remove.append(j)
            for j in to_remove[::-1]:
                del hashes_with_fives[j]

            fives = has_five(hashlib.md5(salt + str(i+1+1000)).hexdigest())
            if fives: hashes_with_fives.append((i+1+1000, fives))

            i += 1
