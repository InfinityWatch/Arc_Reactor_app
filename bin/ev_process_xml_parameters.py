#!/usr/bin/env python

import csv
import sys
import re
import xml.etree.ElementTree as ET

#	<Data Name='param1'>Windows Modules Installer</Data><Data Name='param2'>stopped</Data><Binary>540072007500730074006500640049006E007300740061006C006C00650072002F0031000000</Binary>

def process_xml(xml_info):
    try:
    	xml_result = ""
	root = ET.fromstring("<Data>"+xml_info+"</Data>")
	for child in root:
                #xml_result = xml_result + child.tag + child.attrib + child.text+"\n"
                xml_result = xml_result + child.text + "@"
                #xml_result = xml_result + child.attrib + "\n"
        return xml_result
    except:        
        return "Error: "+xml_info

def main():
    if len(sys.argv) != 3:
        print "Usage: python ev_process_xml_parameters.py [raw_xml_data] [extracted_xml_data]"
        print sys.argv[1]
        print len(sys.argv)
        sys.exit(3)

    raw_xml_data = sys.argv[1]
    extracted_xml_data = sys.argv[2]

    infile = sys.stdin
    outfile = sys.stdout

    r = csv.DictReader(infile)
    header = r.fieldnames

    w = csv.DictWriter(outfile, fieldnames=r.fieldnames)
    w.writeheader()

    for result in r:
        if result[raw_xml_data]:
            result[extracted_xml_data] = process_xml(result[raw_xml_data])			
            #result[extracted_xml_data] = raw_xml_data
            if result[extracted_xml_data]:
                w.writerow(result)

main()
