GPXList README
==============

Introduction
------------

Show basic information about a set of GPS GPX files including an offline lookup of the town or area of the start of the route.

Example
-------

::

  >gpxlist tracks/*
  Filename                          Start time           Start place
  --------------------------------  -------------------  ---------------------------
  london_trinity_buoy_wharf.gpx     2019-12-17 12:11:21  Poplar, England, GB
  xmas_shopping.gpx                 2019-12-21 12:03:31  Barnsbury, England, GB
  london_camden_little_venice.gpx   2022-12-23 12:14:14  Camden Town, England, GB
  london_winter_wonderland.gpx      2022-12-27 14:26:50  London, England, GB
  london_kew.gpx                    2023-12-19 11:55:56  Camden Town, England, GB
  london_ferry_and_pyramid.gpx      2024-04-01 10:24:47  City of London, England, GB

Libraries
---------

This tool uses `gpxpy <https://github.com/tkrajina/gpxpy>`_ to parse GPX logs and `reverse_geocoder <https://github.com/thampiman/reverse-geocoder>`_ to find geographic information.

License
-------

This program is released under license GPLv3.
