#
# Copyright (C) 2018 Satoru SATOH <ssato @ redhat.com>
# License: MIT
#
# pylint: disable=missing-docstring,invalid-name,too-few-public-methods
from __future__ import absolute_import

import anyconfig_ion_backend as TT
import tests.common as TBC

_CNF_S = u"""\
$ion_1_0 {'a':0,'c':5,'b':"bbb",'sect0':{'d':["x","y","z"]}}"""


class HasParserTrait(TBC.HasParserTrait):

    psr = TT.Parser()
    cnf = {u"a": 0, u"b": u"bbb", u"c": 5,
           u"sect0": {u"d": [u"x", u"y", u"z"]}}
    cnf_s = TBC._bytes(_CNF_S)


class Test_10(TBC.Test_10_dumps_and_loads, HasParserTrait):

    load_options = dump_options = dict(sort_keys=False)


class Test_20(TBC.Test_20_dump_and_load, HasParserTrait):

    pass

# vim:sw=4:ts=4:et:
