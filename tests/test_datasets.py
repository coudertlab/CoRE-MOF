def test_datasets():
    import CoRE_MOF
    x = CoRE_MOF.list_structures("2014")
    assert isinstance(x, list)
    assert len(x) == 4764
