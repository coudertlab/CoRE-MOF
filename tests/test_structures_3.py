import os
import pytest


def test_structures_1():
    import CoRE_MOF

    x = CoRE_MOF.list_structures("2019-ASR")
    assert "1499489-acs.cgd.6b01265_1499490_clean" in x
    assert "ZUZZEB_clean" in x

    s = CoRE_MOF.get_CIF_structure_data("2019-ASR", "1499489-acs.cgd.6b01265_1499490_clean")
    assert isinstance(s, bytes)
    string = s.decode('utf-8')
    assert "_cell_length_a" in string
    assert "_atom_site_fract_x" in string

    s = CoRE_MOF.get_CIF_structure_data("2019-ASR", "ZUZZEB_clean")
    assert isinstance(s, bytes)
    string = s.decode('utf-8')
    assert "_cell_length_a" in string
    assert "_atom_site_fract_x" in string


def test_structures_2():
    import CoRE_MOF

    with pytest.raises(KeyError):
        CoRE_MOF.get_CIF_structure_data("2019-ASR", "trucmuche")
    with pytest.raises(KeyError):
        CoRE_MOF.get_CIF_structure_data("2019-WTF", "ZUZZEB_clean")


def test_structures_3():
    import CoRE_MOF

    x = CoRE_MOF.list_structures("2019-ASR")
    assert "1499489-acs.cgd.6b01265_1499490_clean" in x
    assert "ZUZZEB_clean" in x

    s = CoRE_MOF.get_CIF_structure_data("2019-ASR", "1499489-acs.cgd.6b01265_1499490_clean")
    assert isinstance(s, bytes)

    with CoRE_MOF.get_CIF_structure_file("2019-ASR", "1499489-acs.cgd.6b01265_1499490_clean") as fname:
        assert os.path.isfile(fname)
        with open(fname, 'rb') as file:
            # Content is the same as the other method
            s2 = file.read()
            assert s2 == s

    # Temporary file is automatically removed
    assert not os.path.isfile(fname)
