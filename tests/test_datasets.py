import pytest


def test_datasets_1():
    from CoRE_MOF import list_datasets
    x = list_datasets()
    assert isinstance(x, list)
    assert len(x) == 3


def test_datasets_2():
    import CoRE_MOF
    for x in CoRE_MOF.list_datasets():
        z = CoRE_MOF.list_structures(x)
        assert isinstance(z, list)
        assert len(z) > 100


def test_datasets_3():
    import CoRE_MOF

    x = CoRE_MOF.list_structures("2014")
    assert isinstance(x, list)
    assert len(x) == 4764

    x = CoRE_MOF.list_structures("2019-ASR")
    assert isinstance(x, list)
    assert len(x) == 12020

    x = CoRE_MOF.list_structures("2019-FSR")
    assert isinstance(x, list)
    assert len(x) == 7061


def test_datasets_4():
    import CoRE_MOF

    with pytest.raises(KeyError):
        s = CoRE_MOF.list_structures("toto")
