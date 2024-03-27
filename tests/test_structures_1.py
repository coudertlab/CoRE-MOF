import math
import pytest


@pytest.mark.filterwarnings("ignore:.*rounded to ideal values")
def test_structures_1():
    import CoRE_MOF
    from pymatgen.core import Structure

    x = CoRE_MOF.list_structures("2019-ASR")
    assert "1499489-acs.cgd.6b01265_1499490_clean" in x
    assert "ZUZZEB_clean" in x

    s = CoRE_MOF.get_structure("2019-ASR", "1499489-acs.cgd.6b01265_1499490_clean")
    assert isinstance(s, Structure)
    a, b, c = s.lattice.abc
    assert math.isclose(a, 18.975)
    assert math.isclose(b, 18.975)
    assert math.isclose(c, 44.763)
    alpha, beta, gamma = s.lattice.angles
    assert math.isclose(alpha, 90)
    assert math.isclose(beta, 90)
    assert math.isclose(gamma, 120)
    assert s.num_sites == 756

    s = CoRE_MOF.get_structure("2019-ASR", "ZUZZEB_clean")
    assert isinstance(s, Structure)
    a, b, c = s.lattice.abc
    assert math.isclose(a, 29.311)
    assert math.isclose(b, 29.311)
    assert math.isclose(c, 29.311)
    alpha, beta, gamma = s.lattice.angles
    assert math.isclose(alpha, 90)
    assert math.isclose(beta, 90)
    assert math.isclose(gamma, 90)
    assert s.num_sites == 936


def test_structures_2():
    import CoRE_MOF

    with pytest.raises(KeyError):
        CoRE_MOF.get_structure("2019-ASR", "trucmuche")
    with pytest.raises(KeyError):
        CoRE_MOF.get_structure("2019-WTF", "ZUZZEB_clean")
