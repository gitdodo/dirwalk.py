#!/usr/bin/python

f = open('workfile.txt', 'w')

import os
import fnmatch

for root, dir, files in os.walk(u"W:/Technical Services/"):
        f.write(root)
        f.write("\n")
        for items in fnmatch.filter(files, "*"):
                f.write("..." + items + "\n")
        f.write("\n")
f.close()
