#!/usr/bin/env python
# Gulp is owned by Phillip Marshall.
# It's free for personal use, but for now he reserves all rights.
# Everything else belongs to Whiskey Media. Please don't sue me.
"""Gulp, a video downloader for Whiksey Media video content."""

import sys
import os
import argparse

try:
    os.chdir(os.path.dirname(__file__))
except NameError:
    print 'Warning: Can\'t cd to the right dir, let\'s hope it works anyways.'

from code import login
from conf.user import USER

parser = argparse.ArgumentParser(description=__doc__)

args = parser.parse_args()

#Do stuff here...

if login.login(USER):
    "yup, logged in."
else:
    "try again duder."
