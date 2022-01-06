from abc import ABC, abstractmethod

class Wire():
    def __init__(self, name, width, is_input, activity_cycle_index):
        self.m_name = name
        self.m_width = width
        self.m_is_input = is_input
        self.m_activity_cycle_index = activity_cycle_index


class AbstractModule(ABC):

    def __init__(self):
        self.m_wires = []
        self.define_core_parameters()
        self.define_interface()
        self.print_wires()

    @abstractmethod
    def define_core_parameters(self):
        pass

    @abstractmethod
    def define_interface(self):
        pass

    def add_wire(self, wire):
        self.m_wires.append(wire)

    def print_wires(self):
        print(f"wires are {self.m_wires}")

    def get_parameters_text(self):
        txt = ""
        for p in self.m_param_dict:
            txt += f"    parameter {p} = -1, \n"
        return txt[:-3]

    def get_ios_text(self):
        txt = ""
        for wire in self.m_wires:
            txt += f"    {'input' if wire.m_is_input else 'output'} wire [{wire.m_width} - 1 : 0] {wire.m_name}, \n"
        return txt[:-3]

    def generate_module_interface(self):
        txt = f"module {self.m_name} #(\n" \
             +f"{self.get_parameters_text()}\n" \
             +f") (\n" \
             +f"{self.get_ios_text()}\n" \
             +f");"
        return txt

    def generate_portfolio(self):
        pass
