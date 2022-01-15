from abc import ABC, abstractmethod
from zelda.module.parameter import Parameter, CoreParameter #, ManualParameter

class Wire():
    def __init__(self, name, width, activity_cycle_index,  is_input):
        self.m_name = name
        self.m_width = width.m_name
        self.m_is_input = is_input
        self.m_activity_cycle_index = activity_cycle_index

class AbstractModule(object):
    def __init__(self):
        self.m_wires = []
        self.m_param_dict = {}
        self.m_localparam_dict = {}
        self.define_interface()

    @abstractmethod
    def define_interface(self):
        pass

    def get_module_implementation(self):
        pass

    def new_core_param(self, name):
        param = CoreParameter(name)
        self.m_param_dict[name] = param
        return param

    def new_wire(self, name, width_param, latency_param, is_input):
        wire = Wire(name, width_param, latency_param, is_input)
        self.m_wires.append(wire)
        return wire

    def new_localparam(self, name, param_expression):
        param_expression.set_name(name)
        self.m_localparam_dict[name] = param_expression
        return param_expression

    def print_wires(self):
        print(f"wires are {self.m_wires}")

    def get_parameters_text(self):
        txt = "    // Core parameters\n"
        for p in self.m_param_dict.values():
            txt += f"    parameter {p.m_name} = -1, \n"
        return txt[:-3]

    def get_localparams_text(self):
        txt = "    // Derived localparams\n"
        for lp in self.m_localparam_dict.values():
            txt += f"    parameter {lp.m_name} = {lp.get_portfolio_function_header(self)}, \n"
        return txt[:-3]

    def get_ios_text(self):
        txt = ""
        for wire in self.m_wires:
            txt += f"    {'input' if wire.m_is_input else 'output'} wire [{wire.m_width} - 1 : 0] {wire.m_name}, \n"
        return txt[:-3]

    def generate_module_interface(self):
        txt = f"module {self.m_name} #(\n" \
             +f"{self.get_parameters_text()}\n" \
             +f"{self.get_localparams_text()}\n" \
             +f") (\n" \
             +f"{self.get_ios_text()}\n" \
             +f");"
        return txt

    def generate_portfolio_function(self, lp):
        if isinstance(lp, CoreParameter):
            raise Exception("Wierd, need to decide what to do")
        func_name = lp.get_portfolio_function_header(self)[:-10]
        txt = "function integer " + func_name + ";\n"
        txt += "    begin\n"
        txt += f"        {func_name} = \n"
        txt += f"{lp.get_portfolio_implementation(self)}"
        txt += "\n    end\nendfunction\n"
        return txt

    def generate_portfolio(self):
        txt = ""
        for lp in self.m_localparam_dict.values():
            txt += self.generate_portfolio_function(lp) + "\n"
        return txt

class AbstractCompositeModule(AbstractModule):
    @abstractmethod
    def define_module_implementation(self):
        pass

    def get_module_implementation(self):
        return "// Automatically deduced implementation based on submodules, currently not implemented" #TODO(gil)

class AbstractAtomicModule(AbstractModule):
    def get_module_implementation(self):
        return "// TODO(you): implement!"

