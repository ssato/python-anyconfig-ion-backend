"""anyconfig backend to load and dump Amazon Ion
(https://http://amzn.github.io) data.
"""
from __future__ import absolute_import
from .ion import Parser

__version__ = "0.0.1"
__all__ = ["Parser"]
