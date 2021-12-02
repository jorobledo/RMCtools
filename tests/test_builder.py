from rmctools import builder


def test_cif_data():
    cif_path = "data/mp-27692_BaB4O7.cif"
    metadata, data = builder.cif_data(cif_path)
    assert isinstance(metadata, dict)
    assert isinstance(data, dict)
    assert len(data.keys()) == 7
    assert len(metadata.keys()) == 12
