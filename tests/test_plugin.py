#
# Copyright (C) 2018 Satoru SATOH <satoru.satoh @ gmail.com>
# License: MIT
#
# pylint: disable=missing-docstring,invalid-name
from __future__ import absolute_import, print_function

import os.path
import os
import unittest

import anyconfig

from tests.common import dicts_equal


_CURDIR = os.path.dirname(__file__)
_CNF_0 = {u'a': 0,
          u'b': u'bbb',
          u'c': 5,
          u'sect0': {u'd': [u'x', u'y', u'z']}}


class Test_90(unittest.TestCase):

    def _try_load(self, fname="ion.txt_data"):
        try:
            filepath = os.path.join(_CURDIR, "res", fname)
            cnf = anyconfig.load(filepath, ac_parser="ion")
        except anyconfig.UnknownFileTypeError:
            print("all types=%r" % anyconfig.list_types())
            raise

        self.assertTrue(dicts_equal(cnf, _CNF_0), "%r vs. %r" % (cnf, _CNF_0))

    def test_90_load_text(self):
        self._try_load()

    def test_92_load_bin(self):
        self._try_load(fname="ion.bin_data")

# vim:sw=4:ts=4:et:
