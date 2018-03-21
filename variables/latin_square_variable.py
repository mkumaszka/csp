from variables.variable import Variable

class Latin_Variable(Variable):

    def __init__(self, graph_size, location):
        super().__init__(graph_size)
        self.location = location
        self.entanglement = self.set_entanglements()

    def set_entanglements(self):
        x_loc = self.location[0]
        y_loc = self.location[1]
        eng_list = [(i, y_loc) for i in range(self.graph_size) if i is not x_loc]
        eng_list.extend([(x_loc, i) for i in range(self.graph_size) if i is not y_loc])
        return eng_list

    def check_variable_constraint(self, variable):
        if variable.value is not None:
            return self.value is not variable.value
        return True

    def create_new_variable(self):
        var = Latin_Variable(self.graph_size, self.location)
        if self.value is not None:
            var.value = self.value
        return var

# variables = []
# for x in range(4):
#     for y in range(4):
#         variables.append(Latin_Variable(4, (x, y)))
#
# print("")
