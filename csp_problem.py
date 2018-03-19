from abc import ABCMeta, abstractmethod
from assignments import Assignment

class CSP_PROBLEM:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, variables):
        self.variables = variables
        self.start = Assignment()

    @abstractmethod
    def check_constraints(self, variable, assignments):
        pass