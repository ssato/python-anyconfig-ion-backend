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

moddir=$(ls -d1 ${topdir}/anyconfig_*_backend/ | head -n 1)

bash ${runtest_sh} ${moddir}
for f in $(echo ${topdir}/tests/*.py | sort); do
    bash ${runtest_sh} $f
done

#coverage run --source=${moddir},tests/
#coverage report -m

# vim:sw=4:ts=4:et:
