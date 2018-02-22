#!/usr/bin/python

import os

print "Content-type: text/html\n\n";
print "<html><head></head>"
print "<body bgcolor='#dddddd'>"

http = r'http://'
http_host = os.environ['HTTP_HOST']
script_name = os.environ['SCRIPT_NAME']
this_script = http + http_host + script_name

print "\n<BR><b>This script:</b><BR>", this_script
print "</body></html>"


