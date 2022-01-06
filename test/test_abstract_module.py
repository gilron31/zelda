import pytest
from zelda.module.module import AbstractModule, Wire

class ExampleModule(AbstractModule):
    def __init__(self, name, param_dict):
        AbstractModule.__init__(self)
        self.m_param_dict = param_dict
        self.define_interface()
        self.print_wires()
        self.m_name = name
        print("Hi am example module")

    def define_interface(self):
        self.add_wire(Wire("IN", self.m_param_dict["P_WIDTH"], True, 0))
        self.add_wire(Wire("OUT", self.m_param_dict["P_WIDTH"], False, 2))
        print("defined the interface")



def test_abstract_module():
    param_dict = {"P_WIDTH" : "P_WIDTH", "P_NUM_SCHIN" : "P_NUM_SCHIN"}
    em = ExampleModule("example_module_1", param_dict)
    em.print_module_interface()
    print("TESTED")