from submission import Submission

class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):

        def check(enc, checksum):
            count = { chr(i) : 0 for i in range(ord('a'), ord('z')+1) }
            for c in enc:
                if c != ' ':
                    count[c] += 1

            realchecksum = ''
            for i in range(5):
                maxc = None
                for c in count:
                    if maxc is None or count[maxc] < count[c]:
                        maxc = c
                    elif count[maxc] == count[c] and ord(c) < ord(maxc):
                        maxc = c
                realchecksum += str(maxc)
                del count[maxc]

            return realchecksum == checksum

        def decrypt(enc, sectionID):
            dec = ''
            for c in enc:
                if c != ' ':
                    dec += str(chr((ord(c) - ord('a') + sectionID) % 26 + ord('a')))
            return dec

        for line in s.rstrip().split("\n"):
            enc = ' '.join(line[:-7].split('-')[:-1])
            sectionID = int(line[:-7].split('-')[-1])
            checksum = line[-6:-1]
            if check(enc, checksum):
                if decrypt(enc, sectionID) == "northpoleobjectstorage":
                    return sectionID
