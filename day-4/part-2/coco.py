import re, collections

from submission import Submission

class CocoDay4Part2(Submission):

    def author(self):
        return"coco"

    def run(self, instructions):
        regex = "(.*)-([0-9]*)\[([a-z]*)\]"
        for line in instructions.strip().split('\n'):
            m = re.search(regex, line)
            name, room_id, checksum = m.groups()
            new_name = "".join(map(lambda char: " " if char == "-" else chr( ord('a') + (ord(char) - ord('a') + int(room_id)) % 26), name))
            if 'northpole' in new_name:
                return int(room_id)
