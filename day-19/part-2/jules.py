from submission import Submission

class JulesSubmission(Submission):

    def author(self):
        return 'Jules'

    def run(self, s):
        nb = int(s.strip())
        import collections
        left = collections.deque()
        right = collections.deque()

        # we place half first elements in left, other in right
        for i in range(nb/2 + 1):
            left.append(i)
        for i in range(nb, nb / 2, -1):
            right.append(i)

        while left and right:
            #We remove the element in front of the first element. This element is the last element of the largest queue
            if len(left) > len(right):
                left.pop()
            else:
                right.pop()
            #Then we rotate everything to the left. first element of left becomes first element of right
            #Last element of right becomes last element of left
            right.appendleft(left.popleft())
            left.append(right.pop())

        if len(left) > 0:
            return left[0]
        else:
            return right[0]
