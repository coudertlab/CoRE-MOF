from . import data

import contextlib
from importlib import resources
import os
import tarfile
import tempfile


# List of datasets available, and corresponding file
__datasets = {
    "2014": "2014.tar.xz",
    "2019-ASR": "2019-ASR.tar.xz",
    "2019-FSR": "2019-FSR.tar.xz",
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

    path = resources.files(data) / __datasets[dataset]
    with tarfile.open(path, 'r') as tar:
        # Select nonempty regular .cif files
        res = [x.name for x in tar.getmembers()
               if x.size > 0 and x.isfile() and x.name.endswith('.cif')]
        # Forget directory structure
        res = [x.split('/')[-1] for x in res]
        # Files starting with . are macOS tar pseudo-files
        res = [x for x in res if x[0] != '.']

    if len(set(res)) != len(res):
        raise ValueError("dataset contains duplicate entries")

    __dataset_structlist[dataset] = res
    return res


def get_CIF_structure_data(dataset, entry):
    """
    Extract a single CIF file from a dataset, as data
    """

    if dataset not in __datasets:
        raise KeyError("unknown dataset")

    path = resources.files(data) / __datasets[dataset]
    member = None
    with tarfile.open(path, 'r') as tar:
        for x in tar.getmembers():
            if x.size > 0 and x.isfile() and x.name.endswith(entry):
                member = x

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
