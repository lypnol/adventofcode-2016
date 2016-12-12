import re

from submission import Submission

class CocoDay8Part1(Submission):

    screen = []
    x = 50
    y = 6

    reg_rect = "rect ([0-9]*)x([0-9]*)"
    reg_row = "rotate row y=([0-9]*) by ([0-9]*)"
    reg_col = "rotate column x=([0-9]*) by ([0-9]*)"


    def author(self):
        return "coco"

    def run(self, instructions):
        # instructions = "rect 3x2\nrotate column x=1 by 1\nrotate row y=0 by 4\nrotate column x=1 by 1"
        self.init_screen(self.x, self.y)
        for line in instructions.strip().split("\n"):
            m = re.search(self.reg_rect, line)
            if m:
                x, y = m.groups()
                self.rect(int(x), int(y))
                continue
            m = re.search(self.reg_row, line)
            if m:
                y, n = m.groups()
                self.rotate_row(int(y), int(n))
                continue
            m = re.search(self.reg_col, line)
            if m:
                x, n = m.groups()
                self.rotate_col(int(x), int(n))
                continue
        # self.print_screen()
        return len([1 for y in self.screen for x in y if x])


    def init_screen(self, x, y):
        self.screen = []
        for i in range(y):
            line = [False] * x
            self.screen.append(line)

    def print_screen(self):
        print("=" * self.x)
        for line in self.screen:
            print("".join(["#" if a == True else " " for a in line]))
        print("=" * self.x)

    def rect(self, x, y):
        for i in range(y):
            for j in range(x):
                self.screen[i][j] = True

    def rotate_col(self, x, n):
        for _ in range(n):
            temp = self.screen[self.y - 1][x]
            for i in range(self.y - 1, 0, -1):
                self.screen[i][x] = self.screen[i-1][x]
            self.screen[0][x] = temp

    def rotate_row(self, y , n):
        self.screen[y] = self.screen[y][self.x - n:self.x] + self.screen[y][:self.x - n]
