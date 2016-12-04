from submission import Submission

class JulesSubmission(Submission):

    def author(self):
        return 'Jules'

    def run(self, s):
        import string

        charset = string.ascii_lowercase
        totalCount = 0

        for line in s.rstrip().split('\n'):
            count = [(0,'')] * len(charset)
            elements = line.split('-')
            id,checksum = elements[-1].split('[')
            checksum = checksum[:-1]
            for word in elements[:-1]:
                for c in word:
                    count[charset.index(c)] = (count[charset.index(c)][0]+1,c)

            newChecksum = ""
            for _,char in sorted(count, key=lambda x: (-x[0],x[1]))[:5]: #Descending for number, ascending for letter
                newChecksum += char

            if newChecksum == checksum:
                totalCount += int(id)

        return totalCount