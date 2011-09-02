#!/usr/bin/env python
import os
import re

COOKIEFILE = 'conf/cookies'
HTMLFILE = 'temp.html'

def wget(url, usecookies=True, args=''):
    call = 'wget --output-document=%s ' % HTMLFILE
    if usecookies:
        call += '--load-cookies %s --save-cookies %s --keep-session-cookies ' % (COOKIEFILE, COOKIEFILE)
    if args:
        call += '%s ' % args
    call += url
    return os.system(call)

def searchinfile(filename, q):
    openfile = open (filename, 'r')
    match=re.search(q, openfile.read())
    openfile.close()
    return match
