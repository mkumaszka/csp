class Variable:

    def __init__(self, graph_size):
        self.value = None
        self.graph_size = graph_size #liczba kratek w jedną stronę
        # self.domain = range(graph_size*graph_size)
        self.domain = list(range(8))

    def extend_domain(self):
        return self.domain.append(len(self.domain))

def extend_var_domain(variable):
    return variable.domain.append(len(variable.domain))




