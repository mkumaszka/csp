from variables.variable import Variable

class CSP_Variable(Variable):

    def __init__(self, graph_size, location):
        super().__init__(graph_size)
        self.location = location
        self.entanglement = self.set_entanglements()

    def locs_diff_2(self):
        x = self.location[0]
        y = self.location[1]
        return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    def locs_diff_1(self):
        x = self.location[0]
        y = self.location[1]
        return [(x + 2, y), (x - 2, y), (x, y + 2), (x, y - 2), (x+1, y-1), (x-1, y+1), (x+1, y+1), (x-1, y-1)]

    def set_entanglements(self):
        eng_1 = self.set_entanglements_for_locs(self.locs_diff_1())
        eng_2 = self.set_entanglements_for_locs(self.locs_diff_2())
        return {1: eng_1, 2: eng_2}

    def check_variable_diff(self, diff, var):
        try:
            return abs(var.value - self.value) >= diff
        except Exception:
            return True

    def set_entanglements_for_locs(self, locs):
        eng_list = []
        for _x, _y in locs:
            if 0 <= _x < self.graph_size and 0 <= _y < self.graph_size:
                eng_list.append((_x, _y))
        return eng_list

    def create_new_variable(self):
        var = CSP_Variable(self.graph_size, self.location)
        if self.value is not None:
            var.value = self.value
        return var

variables = []
for x in range(4):
    for y in range(4):
        variables.append(CSP_Variable(4, (x, y)))
