try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from fabric_contrib import __version__

setup(
    name='fabric-conrib',
    version=__version__,
    author='Ivan Yurin',
    url='https://github.com/astrastudio/fabric-contrib/',
    packages=["fabric_conrib"],
    platforms="Posix; MacOS X; Windows",
)
