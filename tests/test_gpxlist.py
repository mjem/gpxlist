#!/usr/bin/env python3

"""Basic tests of decoding simpler routes."""

import warnings

# pytest_shell needs something that will be removed in Python 3.13
warnings.simplefilter("ignore")

from pytest_shell.shell import bash
# from pytest_resource_path import resource_path

def test_help(bash):
	bash.run_script("gpxlist", ["--help"])

def test_version(bash):
	bash.run_script("gpxlist", ["--version"])
	# assert bash.run_script("gpxlist --version") == "xxx"

def test_decode(bash):  # , resource_path):
	assert bash.run_script("gpxlist", ["tests/tondon.gpx"]) == \
"""Filename    Start time           Start place
----------  -------------------  -------------------
tondon.gpx  2021-10-01 11:11:49  London, England, GB"""
