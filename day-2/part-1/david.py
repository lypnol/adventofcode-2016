from submission import Submission

class DavidSubmission(Submission):
    def author(s):
        return 'David'


    # Returns the last button
    def follow_instructions(self, start_button, instructions):
        button_pos = {'x' : (start_button-1) % 3, 'y': (start_button-1) / 3}
        for instruction in instructions:
            if instruction == 'L' and button_pos['x'] > 0:
                button_pos['x'] -= 1
            elif instruction == 'R' and button_pos['x'] < 2:
                button_pos['x'] += 1
            elif instruction == 'U' and button_pos['y'] > 0:
                button_pos['y'] -= 1
            elif instruction == 'D' and button_pos['y'] < 2:
                button_pos['y'] += 1

        return button_pos['y']*3 + button_pos['x'] + 1

    def run(self, s):
        answer = ''
        button = 5
        for instructions_line in s.strip().split('\n'):
            button = self.follow_instructions(button, instructions_line)
            answer += str(button)

        return ''.join(answer)
