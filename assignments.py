
class Assignment:

    def __init__(self):
        self.assignments = []

    def from_another(self, assignment):
        for var in assignment:
            self.assignments.append(var)

    def add_assignment(self, variable):
        self.assignments.append(variable)

    def get_unassigned_variable(self):
        for var in self.assignments:
            if var.value is None:
                return var