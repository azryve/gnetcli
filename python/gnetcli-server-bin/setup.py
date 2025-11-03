# setup.py
from setuptools import setup
from setuptools.dist import Distribution

class BinaryDistribution(Distribution):
    def has_ext_modules(self):
        # Tells wheel: not a pure-Python dist -> produce platform tag
        return True
    def is_pure(self):
        return False

setup(distclass=BinaryDistribution)
