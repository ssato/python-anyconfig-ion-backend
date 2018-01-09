"""anyconfig backend to load and dump Amazon Ion
(https://http://amzn.github.io) data.
"""
from __future__ import absolute_import
from .ion import Parser

__all__ = ["Parser"]
