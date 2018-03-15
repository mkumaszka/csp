

class Variable:

    def __init__(self, graph_size):
        self.value = None
        self.graph_size = graph_size #liczba kratek w jedną stronę
        self.domain = range(graph_size*graph_size)
        self.domain_dict = self.create_domain_dict()

    def create_domain_dict(self):
        return {x: False for x in self.domain}

    def visit_value(self, value):
        #check if value in dict!!!!
        self.domain_dict[value] = True

    def reset_dict(self):
        self.domain_dict = self.create_domain_dict()

    def check_variable_diff(self, diff, var):
        try:
            return abs(var.value - self.value) >= diff
        except Exception:
            return True





