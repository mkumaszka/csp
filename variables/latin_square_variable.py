from variables.variable import Variable

class Latin_Variable(Variable):

    def __init__(self, graph_size, location, domain):
        super().__init__(graph_size, domain)
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

    def check_variable_constraint_with_value(self, variable, new_value):
        if variable.value is not None:
            return new_value is not variable.value
        return True

    def create_new_variable(self):
        var = Latin_Variable(self.graph_size, self.location, len(self.domain))
        if self.value is not None:
            var.value = self.value
        var.domain = self.domain
        return var

    def restrict_domain(self, new_variable):
        new_domain = []
        if new_variable.location not in self.entanglement:
            return None
        for val in self.domain:
            if self.check_variable_constraint_with_value(new_variable, val):
                new_domain.append(val)
        self.domain = new_domain
