import pytest
from zelda.module.module import AbstractAtomicModule, Wire


class ExampleModule(AbstractAtomicModule):

    def define_core_parameters(self):
        self.m_param_dict = {"P_WIDTH": "P_WIDTH", "P_NUM_SCHIN": "P_NUM_SCHIN"}
        self.m_name = "my_example_module_1"
        print("Hi am example module")

    def define_interface(self):
        '''
        Your module has a few parameters on which it depends.
        These parameters are the ones indicated in the __init__
        you've defined.
        As a HW developer, the widths and desired latencies of your module's
        ports are determined by your implementation, which is in turn
        determined by the modules parameters. You are the only entity
        which is aware of the widths and latencies dependence on the parameters,
        It therefore only makes sense that you need to write them down explicitly.

        '''

        self.add_wire(Wire("IN", self.m_param_dict["P_WIDTH"], True, 0))
        self.add_wire(Wire("AUX_1", self.m_param_dict["P_WIDTH"], True, 0))
        self.add_wire(Wire("OUT", self.m_param_dict["P_WIDTH"], False, 2))
        print("defined the interface")


def test_abstract_module():
    print("\n=========== START TEST ===========")
    em = ExampleModule()
    print(em.generate_module_interface())
    print(  "============ END TEST ============")
