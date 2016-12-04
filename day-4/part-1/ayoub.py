from submission import Submission

class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):

        def check(enc, checksum):
            count = { chr(i) : 0 for i in range(ord('a'), ord('z')+1) }
            for c in enc:
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

        count = 0
        for line in s.rstrip().split("\n"):
            enc = ''.join(line[:-7].split('-')[:-1])
            sectionID = int(line[:-7].split('-')[-1])
            checksum = line[-6:-1]
            if check(enc, checksum):
                count += sectionID

        return count
