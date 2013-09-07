from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
setup(
    name = "dF",
    version = "0.0.1",
    packages = find_packages(),
    scripts = ['scripts/dF', 'scripts/dF-gui'],

    url = 'http://github.com/Pringley/dF',
    
    author = "Ben Pringle",
    author_email = "ben.pringle@gmail.com",
    description = "FATE dice roller",
    license = "MIT",
)
