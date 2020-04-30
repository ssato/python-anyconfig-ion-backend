"""anyconfig backend to load and dump Amazon Ion
(https://http://amzn.github.io) data.
"""
from __future__ import absolute_import
from .ion_ import Parser

__version__ = "0.1.1"
__all__ = ["Parser"]
