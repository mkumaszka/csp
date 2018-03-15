from variable import Variable
from color_graph_problem import ColorGraphProblem

class CSP_Variable(Variable):

    def __init__(self, domain, location):
        super().__init__(domain)
        self.location = location
        self.entanglement = self.set_entanglements()

    def locs_diff_1(self):
        x = self.location[0]
        y = self.location[1]
        return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    def locs_diff_2(self):
        x = self.location[0]
        y = self.location[1]
        return [(x + 2, y), (x - 2, y), (x, y + 2), (x, y - 2), (x+1, y-1), (x-1, y+1), (x+1, y+1), (x-1, y-1)]

    def set_entanglements(self):
        eng_1 = self.set_entanglements_for_locs(self.locs_diff_1())
        eng_2 = self.set_entanglements_for_locs(self.locs_diff_2())
        return {1: eng_1, 2: eng_2}

    def set_entanglements_for_locs(self, locs):
        eng_list = []
        for _x, _y in locs:
            if 0 <= _x < self.graph_size and 0 <= _y < self.graph_size:
                eng_list.append((_x, _y))
        return eng_list

variables = []
for x in range(4):
    for y in range(4):
        variables.append(CSP_Variable(4, (x, y)))

variables[0].value = 0
variables[1].value = 0
assignments = [variables[0], variables[1]]

problem = ColorGraphProblem(variables)
print(problem.check_constraints(variables[0], assignments))


