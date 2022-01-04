import os

from rmctools import builder

cif_path = "data/mp-27692_BaB4O7.cif"


def test_cif_data():
    metadata, data = builder.cif_data(cif_path)
    assert isinstance(metadata, dict)
    assert isinstance(data, dict)
    assert len(data.keys()) == 7
    assert len(metadata.keys()) == 12


def test_max_n():
    struc = builder.load_structure(cif_path)
    assert builder.max_n(struc, 10000) == 4


def test_sc():
    struc = builder.load_structure(cif_path)

    arr = builder.sc(
        struc, n=builder.max_n(struc, 10000), save=False, centred=True
    )

    arr2 = builder.sc(
        struc, n=builder.max_n(struc, 10000), save=True, centred=False
    )

    PATH = "./struc.txt"
    assert os.path.isfile(PATH) and os.access(PATH, os.R_OK)
    os.remove(PATH)
    assert arr.shape == arr2.shape
    assert arr[0].__repr__() == "('B', -20.58015, -14.889754, -20.284002)"
    assert arr2[0].__repr__() == "('B', 0.10650984, 1.8070474, 5.8723216)"
