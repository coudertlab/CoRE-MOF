import pytest
import random


def func_check_random_structs(dataset):
    import CoRE_MOF

    for i in random.choices(CoRE_MOF.list_structures(dataset), k=5):
        s = CoRE_MOF.get_structure(dataset, i)
        assert sum(s.pbc) == 3
        assert s.num_sites > 1
        assert s.n_elems > 1
        assert s.volume > 10
        assert ((1 in s.atomic_numbers) or (6 in s.atomic_numbers)
                or (7 in s.atomic_numbers) or (8 in s.atomic_numbers))


@pytest.mark.filterwarnings("ignore:.*rounded to ideal values")
@pytest.mark.filterwarnings("ignore:.*Possible issue in CIF file at line")
def test_random_structures():
    import CoRE_MOF

    for x in CoRE_MOF.list_datasets():
        func_check_random_structs(x)
