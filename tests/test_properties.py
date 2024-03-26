import pandas


def test_properties_1():
    import CoRE_MOF
    for x in CoRE_MOF.list_datasets():
        p = CoRE_MOF.get_properties(x)
        assert isinstance(p, pandas.DataFrame)
        assert len(p) == len(CoRE_MOF.list_structures(x))


def test_properties_2():
    import CoRE_MOF
    p = CoRE_MOF.get_properties("2019-ASR")
    assert p.shape == (12020, 42)
    columns = p.columns.tolist()
    assert "filename" in columns
    assert "LCD" in columns
    assert "ASA_m2_cm3" in columns
    assert p["LCD"].min() < 3
    assert p["LCD"].max() > 30
