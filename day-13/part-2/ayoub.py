from submission import Submission


class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        s = s.rstrip()
        N = int(s)
        start = 1, 1
        goal = 31,39

        def is_wall(x, y):
            r = x*x + 3*x + 2*x*y + y + y*y
            r += N
            return bin(r).count("1") % 2 == 1

        dist = {start: 0}
        queue = [start]
        visited = set()
        while queue:
            (x, y) = queue.pop(0)
            visited.add((x, y))
            for u,v in [(1,0), (0,1), (-1,0), (0, -1)]:
                node = (x+u, y+v)
                if x+u >= 0 and y+v >=0 and\
                 not is_wall(*node) and node not in visited:
                    if node not in dist or dist[node] < dist[(x,y)] + 1:
                        dist[node] = dist[(x,y)] + 1
                        for i, n in enumerate(queue):
                            if n == node:
                                queue.pop(i)
                                break
                        if dist[node] <= 50:
                            queue.append(node)

        return len(visited)
