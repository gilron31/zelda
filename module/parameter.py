from abc import ABC, abstractmethod
# from zelda.module.module import AbstractModule

class Parameter(ABC):
    def __init__(self, name : str):
        self.m_name = name

    def set_name(self, name : str):
        self.m_name = name

    def __add__(self, other):
        if isinstance(other, int):
            return AddParameters([self, LiteralParameter(other)])
        elif isinstance(other, Parameter):
            return AddParameters([self, other])
        else:
            raise Exception("Parameter added with non-parameter type")

    def __mul__(self, other):
        if isinstance(other, int):
            return MulParameters([self, LiteralParameter(other)])
        elif isinstance(other, Parameter):
            return MulParameters([self, other])
        else:
            raise Exception("Parameter added with non-parameter type")

    def __str__(self):
        return self.m_name

    def get_portfolio_implementation(self):
        return self.m_name

    # @abstractmethod
    def get_portfolio_function_header(self, module):
        name_lower = self.m_name[3:].lower()
        return module.m_name + "_get_" + name_lower + "(  TODO  )"  # TODO(gil): fix empty () to list all/dependent paramters


class CompositeParameter(Parameter):
    def __init__(self, args):
        self.m_args = args

class AddParameters(CompositeParameter):
    def get_portfolio_implementation(self, module):
        return f"       {self.m_args[0].get_portfolio_function_header(module)} + \n" +\
               f"       {self.m_args[1].get_portfolio_function_header(module)}"

class MulParameters(CompositeParameter):
    def get_portfolio_implementation(self, module):
        return f"       {self.m_args[0].get_portfolio_function_header(module)} * \n" +\
               f"       {self.m_args[1].get_portfolio_function_header(module)}"

class LiteralParameter(Parameter):
    def __init__(self, val):
        self.m_val = val
        self.m_name = str(val)

    def get_portfolio_function_header(self, module):
        return self.m_name

# class ManualParameter(Parameter):
#     def __init__(self, name):
#         self.m_name = name
#
#     def __str__(self):
#         return self.m_name

class CoreParameter(Parameter):
    def get_portfolio_function_header(self, module):
        return self.m_name
        # raise Exception("Core parameters should never be asked for their portfolio headers")

