from abc import ABC, abstractmethod
from zelda.module.parameter import Parameter, CoreParameter, ManualParameter, LiteralParameter
from zelda.module.file_utils import export_txt_to_file

BACKSLASH_LINE = "/"*50

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
        param = CoreParameter(name, self)
        self.m_param_dict[name] = param
        return param

    def new_wire(self, name, width_param, latency_param, is_input):
        wire = Wire(name, width_param, latency_param, is_input)
        self.m_wires.append(wire)
        return wire

    def new_localparam(self, name, param_expression):
        if isinstance(param_expression, int):
            param_expression = LiteralParameter(param_expression, self)
        param_expression.set_name(name)
        self.m_localparam_dict[name] = param_expression
        return param_expression

    def new_manual_localparam(self, name):
        param_expression = ManualParameter(name, self)
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
            txt += f"    parameter {lp.m_name} = {lp.get_portfolio_function_header()}, \n"
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
        func_name = lp.get_portfolio_function_name()
        txt = "function integer " + func_name + ";\n"
        txt += "    input integer "
        txt += "    input integer ".join([param + ";\n" for param in self.m_param_dict])
        txt += "    begin\n"
        txt += f"        {func_name} = \n"
        txt += f"{lp.get_portfolio_implementation()}"
        txt += "\n    end\nendfunction\n"
        return txt

    def generate_portfolio(self):
        txt = f"{BACKSLASH_LINE}\n// {self.m_name} portfolio\n" + \
              f"// Core parameters are:\n" + \
              "".join([f"//     {param} \n" for param in self.m_param_dict]) + \
              f"{BACKSLASH_LINE}\n\n"
        for lp in self.m_localparam_dict.values():
            txt += self.generate_portfolio_function(lp) + "\n"
        export_txt_to_file(txt, f"{self.m_name}_portfolio.vh")

class AbstractCompositeModule(AbstractModule):
    @abstractmethod
    def define_module_implementation(self):
        pass

    def get_module_implementation(self):
        return "// Automatically deduced implementation based on submodules, currently not implemented" #TODO(gil)

class AbstractAtomicModule(AbstractModule):
    def get_module_implementation(self):
        return "            // TODO(you): implement!"

