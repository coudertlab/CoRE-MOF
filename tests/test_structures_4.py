import pytest


@pytest.mark.filterwarnings("ignore:.*rounded to ideal values")
def test_structures_1():
    import CoRE_MOF

    i = 0
    for name, s in CoRE_MOF.all_structures("2014"):
        i += 1
        assert "H" in s.formula or "C" in s.formula or "O" in s.formula
        assert "_clean" in name or "_charged" in name or "_ion" in name
        if i > 20:
            break
