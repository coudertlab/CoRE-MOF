# CoRE-MOF Python package

![MIT](https://img.shields.io/badge/code_license-MIT-blue)
![CC-BY](https://img.shields.io/badge/data_license-CC_BY_4.0-blue)
![Build status](https://github.com/coudertlab/CoRE-MOF/actions/workflows/python-test.yml/badge.svg)

Easy access to the various versions of the [CoRE MOF databases](https://cmcp-group.github.io/database-tools/),
as a Python package.

Two lines of code give you access to any structure from the databases:

```
import CoRE_MOF
mof = CoRE_MOF.get_structure("2019-ASR", "ZUZZEB_clean")
```

----

## Datasets

### CoRE MOF 2014

In the CoRE-MOF package, this dataset is named `2014`.

- Link to dataset: https://doi.org/10.5281/zenodo.3228673
- Link to published paper: https://doi.org/10.1021/cm502594j
- License of the data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

### CoRE MOF 2019

The 2019 database included in the package is the “public” part of the database,
which is freely available. It is split (as in the original publication) into two
distinct datasets: `2019-ASR` (ASR = All Solvent Removed) and `2019-FSR` (FSR =
Free Solvent Removed).

- Link to dataset (latest version, 1.1.4): https://doi.org/10.5281/zenodo.7691378
- Link to published paper: https://doi.org/10.1021/acs.jced.9b00835
- License of the data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
