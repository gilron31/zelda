from abc import ABC, abstractmethod

class Parameter(ABC):
    def __init__(self, name : str, module):
        self.m_name = name
        self.m_module = module

    def set_name(self, name : str):
        self.m_name = name

    def __add__(self, other):
        if isinstance(other, int):
            other = LiteralParameter(other, self.m_module)
        elif isinstance(other, Parameter):
            pass
        else:
            raise Exception("Parameter added with non-parameter type")
        return AddParameters([self, other], self.m_module)

    def __mul__(self, other):
        if isinstance(other, int):
            other = LiteralParameter(other, self.m_module)
        elif isinstance(other, Parameter):
            pass
        else:
            raise Exception("Parameter multiplied with non-parameter type")
        return MulParameters([self, other], self.m_module)

    def __str__(self):
        return self.m_name

    def get_portfolio_implementation(self):
        # Returns a list
        return [self.m_name]

    def get_portfolio_reference(self):
        # Returns a list
        if self.m_name is None:
            return self.get_portfolio_implementation()
        else:
            return [self.get_portfolio_function_header()]

    def get_portfolio_function_name(self):
        # Returns a string
        name_lower = self.m_name[3:].lower()
        return self.m_module.m_name + "_get_" + name_lower

    def get_portfolio_function_header(self):
        # Returns a string
        return self.get_portfolio_function_name() + "(" + \
        ", ".join([param for param in self.m_module.m_param_dict]) + \
        ")"

class CompositeParameter(Parameter):
    def __init__(self, args, module):
        self.m_args = args
        self.m_module = module
        self.m_name = None

    def get_portfolio_implementation(self):
        l1 = self.m_args[0].get_portfolio_reference()
        l2 = self.m_args[1].get_portfolio_reference()
        l1[-1] += f" {self.get_op()} "
        return l1 + l2

    @abstractmethod
    def get_op(self):
        pass

class AddParameters(CompositeParameter):
    def get_op(self):
        return "+"

class MulParameters(CompositeParameter):
    def get_op(self):
        return "*"

class LiteralParameter(Parameter):
    def __init__(self, val, module):
        self.m_val = val
        self.m_module = module
        self.m_name = None

    def get_portfolio_implementation(self):
        return [f"{str(self.m_val)}"]

class ManualParameter(Parameter):
    def get_portfolio_implementation(self):
        return ["// TODO(you): Implement this"]

class CoreParameter(Parameter):
    def get_portfolio_reference(self):
        return [self.m_name]

    def get_portfolio_function_header(self):
        raise Exception("Core parameters should never be asked for their portfolio headers")

