class Towers:

    def __init__(self, size):
        self.towers = [[], [], []]
        self.size = size
        for i in range(self.size, 0, -1):
            self.towers[0].append(i)

    def solveTower(self, ring, src, target, buff):
        if (ring == 1):
            val = self.towers[src].pop()
            self.towers[target].append(val)
            print "%s placing popping %s from %s onto %s" % ("+--" * ring, val, src, target)
            print "%s %s" % ("+--" * ring, self.towers)

        else:
            self.solveTower(ring - 1, src, buff, target)
            val = self.towers[src].pop()
            self.towers[target].append(val)
            print "%s placing popping %s from %s onto %s" % ("+--" * ring, val, src, target)
            print "%s %s" % ("+--" * ring, self.towers)
            self.solveTower(ring - 1, buff, target, src)

t = Towers(5)
t.towers[0]
print t.towers
t.solveTower(t.size, 0, 1 ,2)
print ""
t = Towers(4)
t.solveTower(t.size, 0, 2, 1)