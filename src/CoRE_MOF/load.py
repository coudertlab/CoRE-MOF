from . import data

import contextlib
import csv
from importlib import resources
import os
import tarfile
import tempfile


# List of datasets available, and corresponding filenames
__datasets = {
    "2014": "2014",
    "2019-ASR": "2019-ASR",
    "2019-FSR": "2019-FSR",
}

# Cache of the structures in each dataset
__dataset_structlist = dict()


def list_datasets():
    """
    List of datasets available
    """

    return list(__datasets.keys())


def list_structures(dataset):
    """
    List of structures available in a given dataset
    """

    if dataset not in __datasets:
        raise KeyError("unknown dataset")

    if dataset in __dataset_structlist:
        return __dataset_structlist[dataset]

    path = resources.files(data) / (__datasets[dataset] + '.csv')
    with open(path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        res = [row[0] for row in reader]

    # Check we have header and remove it
    assert res[0] == "filename"
    res = res[1:]

    if len(set(res)) != len(res):
        raise ValueError("dataset contains duplicate entries")

    __dataset_structlist[dataset] = res
    return res


def get_properties(dataset):
    """
    Return a table of properties for materials in a given
    data, as a pandas.DataFrame object
    """

    import pandas

    if dataset not in __datasets:
        raise KeyError("unknown dataset")

    path = resources.files(data) / (__datasets[dataset] + '.csv')
    return pandas.read_csv(path)


def get_CIF_structure_data(dataset, entry):
    """
    Extract a single CIF file from a dataset, as data
    """

    if dataset not in __datasets:
        raise KeyError("unknown dataset")

    path = resources.files(data) / (__datasets[dataset] + '.tar.xz')
    fname = entry + '.cif'
    member = None
    with tarfile.open(path, 'r') as tar:
        for x in tar.getmembers():
            if x.size > 0 and x.isfile() and x.name.split('/')[-1] == fname:
                member = x
                break

        if member:
            res = tar.extractfile(member).read()
            return res

    raise KeyError("unknown entry in dataset")


@contextlib.contextmanager
def get_CIF_structure_file(dataset, entry):
    """
    Extract a single CIF file from a dataset, as temporary file on disk.
    """

    try:
        res = get_CIF_structure_data(dataset, entry)
        file = tempfile.NamedTemporaryFile(suffix='.cif', delete=False)
        fname = file.name
        file.write(res)
        file.close()
        yield fname
    finally:
        os.unlink(fname)


def get_structure(dataset, entry):
    """
    Extract a single pymatgen Structure from a dataset
    """

    from pymatgen.core import Structure

    res = get_CIF_structure_data(dataset, entry)
    return Structure.from_str(res.decode('utf-8'), fmt='cif')


def all_structures(dataset):
    """
    Iterator over all structures from a chosen dataset,
    as pymatgen Structure objects.

    Warning: This is a slow function, because unpacking
    the entire dataset and parsing all CIF files is slow.
    """

    from pymatgen.core import Structure

    if dataset not in __datasets:
        raise KeyError("unknown dataset")

    path = resources.files(data) / (__datasets[dataset] + '.tar.xz')
    with tarfile.open(path, 'r') as tar:
        for x in tar.getmembers():
            # Select nonempty regular .cif files
            if x.size > 0 and x.isfile() and x.name.endswith('.cif'):
                # Forget directory structure
                name = x.name.split('/')[-1].replace('.cif', '')
                if name[0] != '.':
                    cif = tar.extractfile(x).read()
                    yield name, Structure.from_str(cif.decode('utf-8'), fmt='cif')
