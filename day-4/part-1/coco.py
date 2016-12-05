import re, collections

from submission import Submission

class CocoDay4Part1(Submission):

    def author(self):
        return "coco"

    def run(self, instructions):
        regex = "(.*)-([0-9]*)\[([a-z]*)\]"
        total = 0
        for line in instructions.strip().split('\n'):
            m = re.search(regex, line)
            name, room_id, checksum = m.groups()
            c = collections.Counter(name.replace("-", ""))
            most_commons = c.most_common()
            letters = sorted(most_commons, key=lambda x: x[0])
            letters = sorted(letters, key=lambda x: x[1], reverse=True)
            correct_checksum = "".join(letter[0] for letter in letters[:5])
            if correct_checksum == checksum:
                total += int(room_id)
        return total
