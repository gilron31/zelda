
class Parameter(object):
    def __init__(self, op : str, args):
        self.m_op = op
        self.m_args = args

    def set_name(self, name : str):
        self.m_name = name

    def __add__(self, other):
        return Parameter("ADD", [self, other])

    def __mul__(self, other):
        return Parameter("MUL", [self, other])

    def __str__(self):
        if self.m_op == 'ADD':
            return "(" + str(self.m_args[0]) + " + " + str(self.m_args[1]) + ")"
        elif self.m_op == 'MUL':
            return "(" + str(self.m_args[0]) + " * " + str(self.m_args[1]) + ")"
        else:
            raise Exception("Unimplemented operation")

class ManualParameter(Parameter):
    def __init__(self, name):
        self.m_name = name

    def __str__(self):
        return self.m_name

class AtomicParameter(Parameter):
    def __init__(self, name):
        self.m_name = name

    def __str__(self):
        return self.m_name
