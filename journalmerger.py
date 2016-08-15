'''
journal-files -> chronological stream of all entries

USAGE:
journalmerger <journalfile1> <journalfile2> [journalfile3 ...]

OUTPUT: text-stream of all journal-entries from all
    journal files in sorted order

MOTIVATION: I wrote this script because a 3-way-vimdiff
    breaks when differently dated journal entries
    occupy the same line

OUTLINE:
---
- import needed libraries
- create a list of all journal files
- read each journal-file into a separate string
- parse all strings into a single list of entries
- sort all entries
- spit return result to stdout
'''

# import needed libraries
import datetime
import sys
# create a list of all journal files
arguments = sys.argv
journalfiles = sys.argv[1:]
print('journalfiles: ' + journalfiles))
# read each journal-file into a separate string
journalstrings = [file(f).read() for f in journalfiles]
print(journalstrings)
# parse all strings into a single list of entries
  # an entry is text in /^\\section
# sort entries
  # timeofentry = datetime.datetime.strpdatetime
# spit return result to stdout
