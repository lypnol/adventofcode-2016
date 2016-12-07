import re, collections

from submission import Submission

class CocoDay7Part1(Submission):

    def author(self):
        return "coco"

    def has_abba(self, string):
        for i in range(len(string) - 3):
            if string[i] == string[i+3] and string[i+1] == string[i+2] and string[i] != string[i+1]:
                return True
        return False

    def run(self, instructions):
        result = 0
        for line in instructions.strip().split("\n"):
            strings = [s2 for s in line.split('[') for s2 in s.split(']') ]
            if not any(map(self.has_abba, strings[1::2])) and any(map(self.has_abba, strings[::2])):
                result += 1
        return result
