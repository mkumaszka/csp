from abc import ABCMeta, abstractmethod
from assignments import Assignment


class CSP_PROBLEM:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, variables):
        self.variables = variables

    @property
    def start(self):
        return Assignment(self.variables)

    @abstractmethod
    def check_constraints(self, variable, assignments):
        pass

    @abstractmethod
    def is_satisfied(self, assignments):
        pass

    def extend_variables_domain(self):
        # map(extend_var_domain, self.variables)
        for var in self.variables:
            var.extend_domain()
