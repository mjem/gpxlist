#!/usr/bin/env python3

"""Basic tests of decoding simpler routes."""

def test_help(bash):
	assert bash.run_script("gpxlist --help") == "xxx"

def test_version(bash):
	assert bash.run_script("gpxlist --version") == "xxx"

def test_decode(bash):
	assert bash.run_script("gpxlist tondon.gpx") == "xxx"
