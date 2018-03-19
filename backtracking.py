from graph_variable import CSP_Variable
from color_graph_problem import ColorGraphProblem
from assignments import Assignment

variables = []
for x in range(4):
    for y in range(4):
        variables.append(CSP_Variable(4, (x, y)))

variables[0].value = 0
variables[1].value = 0
assignments = [variables[0], variables[1]]

problem = ColorGraphProblem(variables)
print(problem.check_constraints(variables[0], assignments))

def solve(self):
    return resursive_solve(self, problem.start)


def resursive_solve(self,assignments):
    ##check if assignments satisfied

    variable = unassigned_variable(assignments)

    if variable is None:
        return None

    values = get_variable_domain(variable)

    for value in values:
        new_assignment = Assignment()
        new_assignment.from_another(assignments)
        variable.value = value
        new_assignment.add_assignment(variable)

        if not problem.check_constraints(variable, assignments):
            continue

        new_assignment = resursive_solve(new_assignment)
        if new_assignment is not None:
            return new_assignment

    return None


def unassigned_variable(assignments):
    return assignments.get_unassigned_variable()


def get_variable_domain(variable):
    return variable.domain