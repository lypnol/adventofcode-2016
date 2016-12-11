from submission import Submission
from collections import defaultdict


bots = dict()
output = dict()
search = (17, 61)
found = -1
stop = False

class Bot(object):

    def __init__(self, i):
        self.i = i
        self.chips = []
        self.give_queue = []
        self.input_queue = []

    def set_input(self, value):
        global search, found, stop

        if not self.chips:
            self.chips.append(value)
            return True
        elif len(self.chips) == 1:
            lower = min(self.chips[0], value)
            higher = max(self.chips[0], value)
            self.chips = [lower, higher]
            if search[0] == lower and search[1] == higher:
                found = self.i
                stop = True
            return True
        return False

    def give(self, low_to, high_to, low_isBot, high_isBot):
        global bots, output

        if len(self.chips) == 2:
            lower, higher = self.chips
            if low_isBot:
                if low_to not in bots:
                    bots[low_to] = Bot(low_to)
                bots[low_to].enqueue('input', lower)
            else:
                if low_to not in output:
                    output[low_to] = 0
                output[low_to] = lower

            if high_isBot:
                if high_to not in bots:
                    bots[high_to] = Bot(high_to)
                bots[high_to].enqueue('input', higher)
            else:
                if high_to not in output:
                    output[high_to] = Bot(high_to)
                output[high_to] = higher

            self.chips = []
            return True
        return False

    def enqueue(self, instruction, *args):
        global stop

        if instruction == 'input':
            value = args[0]
            if not self.set_input(value):
                self.input_queue.append(value)
        elif instruction == 'give':
            if not self.give(*args):
                self.give_queue.append(tuple(args))

        if not stop:
            self.operate()

    def operate(self):
        while self.input_queue:
            if self.set_input(self.input_queue[0]):
                self.input_queue.pop(0)
            else: break
        while self.give_queue:
            if self.give(*self.give_queue[0]):
                self.give_queue.pop(0)
            else: break


class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        global bots, output

        s = s.rstrip()
        commands = s.split('\n')

        bots = dict()
        output = dict()
        search = (17, 61)
        found = -1
        stop = False

        for command in commands:
            tokens = command.split()

            if tokens[0] == 'value':            # input instruction
                botId = int(tokens[-1])
                value = int(tokens[1])
                if botId not in bots:
                    bots[botId] = Bot(botId)
                bots[botId].enqueue('input', value)
            else:                                # give instruction
                botId = int(tokens[1])
                low_to = int(tokens[6])
                high_to = int(tokens[-1])
                low_isBot = tokens[5] == 'bot'
                high_isBot = tokens[-2] == 'bot'
                if botId not in bots:
                    bots[botId] = Bot(botId)
                bots[botId].enqueue('give', low_to, high_to, low_isBot, high_isBot)

        return found
