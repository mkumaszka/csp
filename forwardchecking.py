from assignments import Assignment


class ForwardChecking:

    def __init__(self, problem):
        self.problem = problem
        self.satisfied_assignments = []

    def solve(self):
        return self.resursive_solve(self.problem.start)


    def resursive_solve(self, assignment):
        if self.problem.is_satisfied(assignment.assignments):
            return assignment

        index, variable = self.unassigned_variable(assignment)

        if variable is None:
            print("Leaf")
            return None

        values = self.get_variable_domain(variable)

        for value in values:
            new_assignment = Assignment([])
            new_assignment.fill_from_another(assignment.assignments)
            new_assignment.assignments[index].value = value
            # new_assignment.show()
            self.problem.restrict_domains_for_unassigned(new_assignment.assignments, index)

            if new_assignment.has_empty_domain():
                return None

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
