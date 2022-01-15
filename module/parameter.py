from abc import ABC, abstractmethod
# from zelda.module.module import AbstractModule

class Parameter(ABC):
    def __init__(self, name : str, module):
        self.m_name = name
        self.m_module = module

    def set_name(self, name : str):
        self.m_name = name

    def __add__(self, other):
        if isinstance(other, int):
            other = LiteralParameter(other)
        elif isinstance(other, Parameter):
            pass
        else:
            raise Exception("Parameter added with non-parameter type")
        return AddParameters([self, other], self.m_module)

    def __mul__(self, other):
        if isinstance(other, int):
            other = LiteralParameter(other)
        elif isinstance(other, Parameter):
            pass
        else:
            raise Exception("Parameter multiplied with non-parameter type")
        return MulParameters([self, other], self.m_module)

    def __str__(self):
        return self.m_name

    def get_portfolio_implementation(self):
        return self.m_name

    # @abstractmethod
    def get_portfolio_function_header(self):
        name_lower = self.m_name[3:].lower()
        return self.m_module.m_name + "_get_" + name_lower + "(  TODO  )"  # TODO(gil): fix empty () to list all/dependent paramters


class CompositeParameter(Parameter):
    def __init__(self, args, module):
        self.m_args = args
        self.m_module = module

class AddParameters(CompositeParameter):
    def get_portfolio_implementation(self):
        return f"           {self.m_args[0].get_portfolio_function_header()} + \n" +\
               f"           {self.m_args[1].get_portfolio_function_header()};"

class MulParameters(CompositeParameter):
    def get_portfolio_implementation(self):
        return f"           {self.m_args[0].get_portfolio_function_header()} * \n" +\
               f"           {self.m_args[1].get_portfolio_function_header()};"

class LiteralParameter(Parameter):
    def __init__(self, val):
        self.m_val = val
        self.m_name = str(val)

    def get_portfolio_function_header(self):
        return self.m_name

class ManualParameter(Parameter):
    def get_portfolio_implementation(self):
        return "// TODO(you): Implement this"

class CoreParameter(Parameter):
    def get_portfolio_function_header(self):
        return self.m_name
        # raise Exception("Core parameters should never be asked for their portfolio headers")

