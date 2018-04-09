import numpy as np
import math

class Assignment:

    def __init__(self, variables):
        self.assignments = variables

    def from_another(self, assignment):
        for var in assignment:
            self.assignments.append(var)

    def add_assignment(self, variable):
        self.assignments.append(variable)

    def get_unassigned_variable(self):
        for index, var in enumerate(self.assignments):
            if var.value is None:
                return index, var
        return -1, None

    def show(self):
        size = int(math.sqrt(len(self.assignments)))
        vars = np.empty((size, size))
        for variable in self.assignments:
            vars[variable.location[0]][variable.location[1]] = variable.value
        print(vars)

    def fill_from_another(self, assignments):
        for variable in assignments:
            self.assignments.append(variable.create_new_variable())

    def has_empty_domain(self):
        emptys = list(filter(lambda var: len(var.domain) is 0,self.assignments))
        return len(emptys) > 0

