class Variable:

    def __init__(self, graph_size, domain):
        self.value = None
        self.graph_size = graph_size #liczba kratek w jedną stronę
        self.domain = list(range(domain))

    def extend_domain(self):
        return self.domain.append(len(self.domain))

    def restrict_domain(self, new_variable):
        pass

def extend_var_domain(variable):
    return variable.domain.append(len(variable.domain))




