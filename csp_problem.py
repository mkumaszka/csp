from abc import ABCMeta, abstractmethod

class CSP_PROBLEM:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, variables):
        self.variables = variables

    @abstractmethod
    def check_constraints(self, variable, assignments):
        pass