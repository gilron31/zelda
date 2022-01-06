import pytest
from zelda.module import module

class ExampleModule(module.AbstractModule):
    def __init__(self, paramlist):
        self.m_paramlist = paramlist
        self.define_interface()
        self.print_wires()
        print("Hi am example module")

    def define_interface(self):
        self.m_wires = self.m_paramlist * 100
        print("defined the interface")



def test_abstract_module():
    em = ExampleModule(4)
    print("TESTED")