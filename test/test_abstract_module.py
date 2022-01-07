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
        self.m_name = "my_example_module_1"

        p_width = self.new_core_param("P_WIDTH")
        p_num_schin = self.new_core_param("P_NUM_SCHIN")


        lp_width_reduced = self.new_localparam("LP_WIDTH_REDUCED", p_width + p_num_schin)
        lp_aux_latency = self.new_localparam("LP_AUX_LATENCY", p_num_schin + 4)
        lp_aux_width = self.new_localparam("LP_AUX_WIDTH", p_num_schin * 2)
        lp_random_param = self.new_localparam("LP_RANDOM_PARAM", lp_aux_width * p_num_schin)

        self.new_wire("IN", p_width, 0, True)
        self.new_wire("AUX_1", lp_aux_width, lp_aux_latency, True)
        self.new_wire("OUT", p_num_schin, lp_width_reduced, False)

def test_abstract_module():
    print("\n=========== START TEST ===========")
    em = ExampleModule()
    # print(em.generate_module_interface())
    print(em.generate_portfolio())
    print(  "============ END TEST ============")
