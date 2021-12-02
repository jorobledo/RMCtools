from gemmi import cif


def cif_data(cif_file):
    data = cif.read_file(cif_file)
    block = data.sole_block()

    metadata = {}
    for item in block:
        if item.pair is not None:
            metadata[item.pair[0]] = item.pair[1]

    loop_items = [
        "_atom_site_type_symbol",
        "_atom_site_label",
        "_atom_site_symmetry_multiplicity",
        "_atom_site_fract_x",
        "_atom_site_fract_y",
        "_atom_site_fract_z",
        "_atom_site_occupancy",
    ]
    loop = {}
    for item in loop_items:
        loop[item] = list(block.find_loop(item))
    return metadata, loop
