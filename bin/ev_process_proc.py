#!/usr/bin/env python

import csv
import sys
import re


# arp.exe,Target Discovery,Obtains information about hosts on the local broadcast domain
# New_Process_Name = C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
# C:\Windows\System32\wbem\WmiPrvSE.exe

def process_interesting(full_path_process):
    try:
        process_path_elements = full_path_process.split("\\")
        process = process_path_elements[len(process_path_elements)-1]
        return process
    except:
        return full_path_process

def main():
    if len(sys.argv) != 3:
        print "Usage: python ev_process_proc.py [full_path_process] [process]"
        print sys.argv[1]
        print len(sys.argv)
        sys.exit(1)

    full_path_process = sys.argv[1]
    process = sys.argv[2]

    infile = sys.stdin
    outfile = sys.stdout

    r = csv.DictReader(infile)
    header = r.fieldnames

    w = csv.DictWriter(outfile, fieldnames=r.fieldnames)
    w.writeheader()

    for result in r:
        if result[full_path_process]:
            result[process] = process_interesting(result[full_path_process])			
            if result[process]:
                w.writerow(result)

main()
