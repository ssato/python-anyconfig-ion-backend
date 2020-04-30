================================
python-anyconfig-ion-backend
================================

.. image:: https://img.shields.io/pypi/v/anyconfig-ion-backend.svg
   :target: https://pypi.python.org/pypi/anyconfig-ion-backend/
   :alt: [Latest Version]

.. image:: https://img.shields.io/travis/ssato/python-anyconfig-ion-backend.svg
   :target: https://travis-ci.org/ssato/python-anyconfig-ion-backend
   :alt: Test status

.. image:: https://img.shields.io/coveralls/ssato/python-anyconfig-ion-backend.svg
   :target: https://coveralls.io/r/ssato/python-anyconfig-ion-backend
   :alt: Coverage Status

.. image:: https://landscape.io/github/ssato/python-anyconfig-ion-backend/master/landscape.png
   :target: https://landscape.io/github/ssato/python-anyconfig-ion-backend/master
   :alt: Code Health

This is a backend module for python-anyconfig to support to load and dump
Amazon Ion data files.

- Author: Satoru SATOH <satoru.satoh@gmail.com>
- License: MIT

SEE ALSO:

- python-anyconfig: https://pypi.python.org/pypi/anyconfig
- Amazon Ion: https://amzn.github.io/ion-docs/

Build & Install
================

- Pre-built Binary RPMs from my copr repos, https://copr.fedoraproject.org/coprs/ssato/python-anyconfig/

  ::

      # Example commands to install pre-built RPMs
      $ sudo dnf copr enable ssato/python-anyconfig
      $ sudo dnf install -y python3-anyconfig-ion-backend

- PyPI: pip3 install anyconfig-ion-backend
- pip from git repo: pip3 install git+https://github.com/ssato/python-anyconfig-ion-backend/
- Build SRPMs, RPMs and install it: python3 setup.py bdist_rpm --source-only && mock dist/python3-anyconfig-\*-backend-<ver_dist>.src.rpm
- Others: try usual ways to build and/or install python modules such like 'python setup.py bdist', etc.

.. vim:sw=2:ts=2:et:
