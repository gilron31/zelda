import pytest
from zelda.module.parameter import Parameter, AtomicParameter
def test_parameter1():
    p1 = AtomicParameter("P_1")
    p2 = AtomicParameter("P_2")
    p3 = AtomicParameter("P_3")
    lp1 = p1 + p2
    lp2 = lp1 * (p3 + 14 + 123) * 123
    # lp1.set_name("LP_1")
    print(lp1)
    print(lp2)