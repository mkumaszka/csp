from problems.csp_problem import CSP_PROBLEM


class LatinProblem(CSP_PROBLEM):

    def __init__(self, variables):
        super().__init__(variables)

    def check_constraints(self, variable, assignments):
        for constraint in variable.entanglement:
            if not variable.check_variable_constraint(self.get_variable_at_location(constraint, assignments)):
                return False
        return True

    def get_variable_at_location(self, location, assignments):
        item = [variable for variable in assignments if variable.location == location]
        try:
            return item[0]
        except IndexError:
            return None

    def is_satisfied(self,assignments):
        for variable in assignments:
            if variable.value is None:
                return False
        return True

    def restrict_domains_for_unassigned(self, assignments, index_of_new):
        unassigned_variables = list(filter(lambda var: var.value is None, assignments))
        new_variable = assignments[index_of_new]
        for var in unassigned_variables:
            var.restrict_domain(new_variable)


