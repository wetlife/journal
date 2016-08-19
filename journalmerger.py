''' journal-files -> chronological stream of all entries

USAGE:
journalmerger <journalfile1> <journalfile2> [journalfile3 ...]

OUTPUT: text-stream of all journal-entries from all
    journal files in sorted order

MOTIVATION: I wrote this script because a 3-way-vimdiff
    breaks when differently dated journal entries
    occupy the same line

OUTLINE:
---
-#####  Keep This Script Very Modular  #####-
-#####  So That Data-Mining Can Later  #####-
-#####  Be Built From These Functions  #####-
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
import regexp as re
# create a list of all journal files
arguments = sys.argv
journalfiles = sys.argv[1:]
print('journalfiles: ' + journalfiles)
# read each journal-file into a separate string
journalstring.append(file(f).read() for f in journalfiles)
print(journalstring)
# parse all strings into a single list of entries
  # an entry is text in /^\\section/
prog = re.compile(pattern)
positions = []
while true:
    postions.append(prog.match(journalstring))
# sort entries chronologically
  # timeofentry = datetime.datetime.strpdatetime
# spit return result to stdout
