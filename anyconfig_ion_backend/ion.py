#
# Copyright (C) 2018 Satoru SATOH <ssato @ redhat.com>
# License: MIT
#
# pylint: disable=too-many-ancestors
r"""Amazon Ion backend:

- Format to support: Amazon Ion, http://amzn.github.io/ion-docs/
- Requirements: amazon.ion, https://pypi.python.org/pypi/amazon.ion
- Development Status :: 3 - Alpha
- Limitations: None obvious but it should have some.
- Special options:

  - All options of amazon.ion.simpleion.load{s,} and
    amazon.ion.simpleion.dump{s,} except object_hook should work.

  - See also:
    https://github.com/amzn/ion-python/blob/master/amazon/ion/simpleion.py
"""
from __future__ import absolute_import

import amazon.ion.simpleion as SI
import anyconfig.backend.base

from anyconfig.compat import getargspec, IS_PYTHON_3

if IS_PYTHON_3:
    from io import BytesIO
else:
    from anyconfig.compat import StringIO as BytesIO


class Parser(anyconfig.backend.base.StringStreamFnParser,
             anyconfig.backend.base.BinaryFilesMixin):
    """Parser for Amazon Ion data files.
    """
    _type = "ion"
    _load_opts = [a for a in getargspec(SI.load).args
                  if a not in "fp object_hook".split()]
    _dump_opts = [a for a in getargspec(SI.dump).args
                  if a not in "obj fp".split()]
    _orderd = True
    _dict_opts = ["object_pairs_hook", "object_hook"]

    _load_from_stream_fn = anyconfig.backend.base.to_method(SI.load)
    _dump_to_stream_fn = anyconfig.backend.base.to_method(SI.dump)

    # dumps is implemented in the git HEAD bug not in the released version yet.
    # _dump_to_string_fn = anyconfig.backend.base.to_method(SI.dumps)

    def load_from_string(self, content, container, **kwargs):
        """
        Load configuration data from given string `content`.

        :param content: Configuration string
        :param container: callble to make a container object
        :param kwargs: keyword options passed to `_load_from_string_fn`

        :return: container object holding the configuration data
        """
        return self.load_from_stream(BytesIO(content), container, **kwargs)

    def dump_to_string(self, cnf, **kwargs):
        """
        Dump config `cnf` to a string.

        :param cnf: Configuration data to dump
        :param kwargs: optional keyword parameters to be sanitized :: dict

        :return: Dict-like object holding config parameters
        """
        stream = BytesIO()
        self.dump_to_stream(cnf, stream, **kwargs)
        return stream.getvalue()

# vim:sw=4:ts=4:et:
