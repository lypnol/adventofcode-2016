from submission import Submission


class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        s = s.rstrip()
        a = sorted([(int(x.split('-')[0]), int(x.split('-')[1])) for x in s.split('\n')],
                    key=lambda x: x[0])
        n = len(a)
        count = 0
        current_max = 0

        for i in range(n-1):
            current_max = max(a[i][1] + 1, current_max)
            if not current_max >= a[i+1][0]:
                count += a[i+1][0] - current_max

        count += 4294967295 - current_max + 1

        return count
