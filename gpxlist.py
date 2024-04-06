#!/usr/bin/env python3

"""List info about a set of GPX GPS track files."""

import argparse
from pathlib import Path
from operator import itemgetter
import importlib.metadata

import gpxpy
import reverse_geocoder
from tabulate import tabulate

# Format for displaying timestamps
DISPLAY_TIME = "%Y-%m-%d %H:%M:%S"

class GPXInfo:
	"""Pull info from a GPX file via gpxpy and reverse_geocoder."""
	def __init__(self, filename:Path):
		self.gpx = gpxpy.parse(filename.open("r"))

	def start_time(self):
		"""Retrieve timestamp of first segment of first track."""
		return self.gpx.tracks[0].segments[0].points[0].time

	def start_place_str(self):
		"""Put together a string summarising location of start of track."""
		point = self.gpx.tracks[0].segments[0].points[0]
		place = reverse_geocoder.search([point.latitude, point.longitude], verbose=False)[0]
		bits = [place["name"], place["admin1"], place["cc"]]
		return ", ".join(bits)


def main():
	"""Command line entry point."""
	try:
		version = importlib.metadata.metadata("gpxlist")["version"]
	except importlib.metadata.PackageNotFoundError:
		version = "dev"

	parser = argparse.ArgumentParser(prog="gpxlist")
	parser.add_argument("--version", action="version", version="%(prog)s {v}".format(v=version))
	parser.add_argument("FILES", nargs="+", help="Input file(s)")
	args = parser.parse_args()
	rows = []
	for f in map(Path, args.FILES):
		info = GPXInfo(f)
		rows.append([f.name,
					 info.start_time().strftime(DISPLAY_TIME),
					 info.start_place_str()])

	# sort by start time
	rows.sort(key=itemgetter(1))

	# show basic info about each input file
	print(tabulate(rows, headers=["Filename", "Start time", "Start place"]))

if __name__ == "__main__":
	main()
