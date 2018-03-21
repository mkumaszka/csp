from backtracking import Backtrack
from problems.color_graph_problem import ColorGraphProblem
from variables.graph_variable import CSP_Variable
from variables.latin_square_variable import Latin_Variable
from problems.latin_problem import LatinProblem

def solve_graph():
    variables = []
    for x in range(5):
        for y in range(5):
            variables.append(CSP_Variable(5, (x, y)))

    problem = ColorGraphProblem(variables)
    backtrack = Backtrack(problem)
    solution = backtrack.solve()
    print(solution.show())




def solve_latin():
    variables = []
    for x in range(5):
        for y in range(5):
            variables.append(Latin_Variable(5, (x, y)))

    problem = LatinProblem(variables)
    backtrack = Backtrack(problem)
    solution = backtrack.solve()
    print(solution.show())