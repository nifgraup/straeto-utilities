#!/usr/bin/python

import csv, sys

reader = csv.reader(open(sys.argv[1], 'rb'), delimiter=',')
reader.next() #header

print '<osm generator="csv2osm" version="0.6">'

i = -1

for row in reader:
	print '  <node id="{0}" lat="{1}" lon="{2}" visible="true">'.format(i, row[3], row[4])
	print '    <tag k="name" v="{0}" />'.format(row[2])
	if row[2] != row[1]:
	        print '<tag k="alt_name" v="{0}" />'.format(row[1])
        print '    <tag k="highway" v="bus_stop" />'
        print '    <tag k="public_transport" v="stop_position" />'
        print '    <tag k="bus" v="yes" />'
	print '    <tag k="source" v="straeto" />'
	print '    <tag k="source:date" v="2011-12-23" />'
        print '    <tag k="straeto:BUSFASTNR" v="{0}" />'.format(row[0])
	print '  </node>'
	i = i-1
	
print '</osm>'

