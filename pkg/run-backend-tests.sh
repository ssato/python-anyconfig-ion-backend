#! /bin/bash
#
# It seems that the order of tests (tests/<backend>.py first then
# tests/plugin.py) is important and tess fails if it's not.
# 
# This is an wrapper script for runtest.sh to specify the order of tests by
# filenames explicitly.
#
set -e

curdir=${0%/*}
topdir=${curdir}/../
runtest_sh=${curdir}/runtest.sh

bash ${runtest_sh} ${topdir}/anyconfig_*_backend/
for f in ${topdir}/tests/*.py; do
    bash ${runtest_sh} $f
done

# vim:sw=4:ts=4:et:
