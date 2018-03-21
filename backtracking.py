from assignments import Assignment


class Backtrack:

    def __init__(self, problem):
        self.problem = problem

    def solve(self):
        return self.resursive_solve(self.problem.start)


    def resursive_solve(self, assignment):
        if self.problem.is_satisfied(assignment.assignments):
            return assignment

        index, variable = self.unassigned_variable(assignment)

        if variable is None:
            return None

        values = self.get_variable_domain(variable)

        for value in values:
            new_assignment = Assignment([])
            new_assignment.fill_from_another(assignment.assignments)
            new_assignment.assignments[index].value = value
            new_assignment.show()

            if not self.problem.check_constraints(new_assignment.assignments[index], new_assignment.assignments):
                continue

            new_assignment = self.resursive_solve(new_assignment)
            if new_assignment is not None:
                return new_assignment

        return None


    def unassigned_variable(self,assignments):
        return assignments.get_unassigned_variable()


    def get_variable_domain(self,variable):
        return variable.domain
