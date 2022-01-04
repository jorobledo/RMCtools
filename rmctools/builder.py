from gemmi import cif

import numpy as np

from pyxtal import pyxtal


def cif_data(cif_file):
    """
    Loads a cif file and extracts loops and items as data and metadata.
    returns:
        - metadata : cif header.
        - data : atom loops
    """
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


def load_structure(cif="data/mp-27692_BaB4O7.cif"):
    """Load a crystalline structure from a cif file.

    Args:
        cif (str, optional): path to cif file. Defaults to
        'data/mp-27692_BaB4O7.cif'.
    """

    xtal = pyxtal()
    xtal.from_seed(seed=cif)
    struc = xtal.to_pymatgen()

    return struc


def max_n(struc, num=10000):
    """Calculates the maximum index 'n' of a supercell of size
    n x n x n for which the number of sites does not excede 'num'.

    Args:
        struc (pymatgen.core.structure.Structure): a mutable version
        of pyxtal structure.
        num (int, optional): [description]. Defaults to 10000.
    """
    arr = np.arange(0, num, 1)
    sites = struc.num_sites
    sites_sc = sites * arr ** 3
    max_val = sites_sc <= num
    return np.argmax(sites_sc[max_val])


def sc(struc, n=1, save=False, centred=True):
    """Generates the atomic positions of a supercell of
    size n x n x n from an initial structure given by a
    .cif file.

    Args:
        struc (pyxtal.pyxtal): structure. output of the
        load_structure() method.
        n (int, optional): [description]. Defaults to 1.
        save (bool, optional): whether to save or not the ouput to a file.
        centred (bool, optional): if True gives centered supercell.
    """
    supercell = struc.__mul__(scaling_matrix=n)

    x, y, z, elem = [], [], [], []

    for i in range(0, np.shape(supercell)[0]):
        line = str(supercell[i]).replace("[", "").replace("]", "").split()
        x.append(float(line[0]))
        y.append(float(line[1]))
        z.append(float(line[2]))
        elem.append(line[3])

    cen_x = x - np.max(x) / 2
    cen_y = y - np.max(y) / 2
    cen_z = z - np.max(z) / 2

    if centred:
        arr = np.array(list(zip(elem, cen_x, cen_y, cen_z)), "U3,f,f,f")
        filename = "struc_centred.txt"
    else:
        arr = np.array(list(zip(elem, x, y, z)), "U3,f,f,f")
        filename = "struc.txt"

    if save:
        np.savetxt(
            filename, arr, fmt="%s %.4f %.4f %.4f", header="Elem\tx\ty\tz"
        )

    return arr
