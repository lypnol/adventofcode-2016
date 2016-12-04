import re
from collections import Counter, defaultdict

from submission import Submission


class DavidSubmission(Submission):
    def author(self):
        return 'David'

    def is_real_room(self, letters, checksum):
        count = Counter(letters)

        occurences = defaultdict(list)
        for letter, occ in count.items():
            occurences[occ].append(letter)

        i = 0
        for occ in sorted(occurences.keys())[::-1]:
            j = min(i + len(occurences[occ]), 5)
            if any((letter not in occurences[occ]) for letter in checksum[i:j]):
                return False

            if sorted(checksum[i:j]) != list(checksum[i:j]):
                return False

            if j == 5:
                return True

            i = j


    def run(self, s):
        sum_sector_id = 0
        for room in s.strip().split('\n'):
            regexp = re.match(r"^([a-z-]+)\-([0-9]+)\[([a-z]+)\]$", room)
            room_string, room_id, room_sum = regexp.groups()
            room_letters = [x for x in room_string if x != '-']
            if self.is_real_room(room_letters, room_sum):
                sum_sector_id += int(room_id)

        return str(sum_sector_id)
