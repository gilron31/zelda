import pytest
from zelda.module.module import AbstractAtomicModule, Wire
from zelda.module.parameter import Parameter, AtomicParameter


class ExampleModule(AbstractAtomicModule):
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
        p_width = AtomicParameter("P_WIDTH")
        p_num_schin = AtomicParameter("P_NUM_SCHIN")
        self.m_param_dict = {"P_WIDTH": p_width, "P_NUM_SCHIN": p_num_schin}
        self.m_name = "my_example_module_1"

        lp_width_reduced = p_width + p_num_schin
        lp_aux_latency = p_num_schin + 4
        lp_aux_width = p_num_schin * 2

        self.add_wire(Wire("IN", p_width, True, 0))
        self.add_wire(Wire("AUX_1", lp_aux_width, True, lp_aux_latency))
        self.add_wire(Wire("OUT", p_num_schin, False, lp_width_reduced))
        print("defined the interface")


def test_abstract_module():
    print("\n=========== START TEST ===========")
    em = ExampleModule()
    print(em.generate_module_interface())
    print(  "============ END TEST ============")
