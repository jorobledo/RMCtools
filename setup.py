from setuptools import setup

with open("README.rst", "r") as fp:
    LONG_DESCRIPTION = fp.read()

REQUIREMENTS = ["numpy", "gemmi", "pyxtal", "matplotlib"]

setup(
    name="RMCtools",
    version="0.1.0",
    description=(
        "Python library to create "
        "initial configurations for RMC"
        "and LAMMPS."
    ),
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    install_requires=REQUIREMENTS,
    author="José Robledo, Mauricio Morán",
    author_email="jose.robledo@cab.cnea.gov.ar",
    url="https://github.com/jorobledo/RMCtools",
    py_modules=None,
    packages=["rmctools"],
    include_package_data=True,
    license="The MIT License",
    keywords=["rmc", "lammps", "configuration"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.9",
    ],
)
