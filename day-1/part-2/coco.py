# from submission import Submission

# class CocoDay1Part2:
#
#     def author(self):
#         return"coco"
#
#     def result(self, x,y):
#         return abs(x) + abs(y)
#
#     def run(self, instructions):
#         instructions = [instruction.strip() for instruction in instructions.split(",")]
#         x = 0
#         y = 0
#         direction = 0
#         old_visits = [(0,0)]
#
#         for instruction in instructions:
#             turn = instruction[0]
#             length = instruction[1:]
#             new_x, new_y = 0, 0
#             if turn == "R":
#                 direction = (direction + 1) % 4
#             elif turn == "L":
#                 direction = (direction - 1) % 4
#             if direction == 0:
#                 new_y =  int(length)
#             elif direction == 1:
#                 new_x =  int(length)
#             elif direction == 2:
#                 new_y = - int(length)
#             elif direction == 3:
#                 new_x = - int(length)
#
#             if new_x > 0:
#                 for i in range(1, new_x +1):
#                     if (x +i, y) in old_visits:
#                         return self.result(x + i, y)
#                     old_visits.append((x + i, y))
#             elif new_x < 0:
#                 for i in range(1, -new_x +1):
#                     if (x - i, y) in old_visits:
#                         return self.result(x - i, y)
#                     old_visits.append((x - i, y))
#             elif new_y < 0:
#                 for i in range(1, -new_y +1):
#                     if (x, y - i) in old_visits:
#                         return self.result(x, y)
#                         break
#                     old_visits.append((x, y - i))
#             elif new_y > 0:
#                 for i in range(1, new_y +1):
#                     if (x, y + i) in old_visits:
#                         return self.result(x, y + i)
#                     old_visits.append((x, y + i))
#             x += new_x
#             y += new_y
