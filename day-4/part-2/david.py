import re
from collections import Counter, defaultdict

from submission import Submission


class DavidSubmission(Submission):
    def author(self):
        return 'David'

    def decode_room(self, room_string, room_id):
        result = ''
        for c in room_string:
            if c == '-':
                result += ' '
            else:
                result += chr((((ord(c) - 96) + room_id) % 26) + 96)

        return result

    def run(self, s):
        sum_sector_id = 0
        for room in s.strip().split('\n'):
            regexp = re.match(r"^([a-z-]+)\-([0-9]+)\[([a-z]+)\]$", room)
            room_string, room_id, room_sum = regexp.groups()
            room_letters = [x for x in room_string if x != '-']

            room_name = self.decode_room(room_string, int(room_id))
            if 'northpole' in room_name:
                return room_id
