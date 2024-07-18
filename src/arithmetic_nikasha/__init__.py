"""The initialization script that makes the package importable.
This script MUST be here for the package to be importable."""
from .stuff import add, subtract

__all__ = ['add', 'subtract']

# This __all__ defines the behavior of arithmetic_nikasha import *
