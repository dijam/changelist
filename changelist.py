#!/usr/bin/env python

import argparse
import os
from pprint import pprint
from git import *
import re
import json
import sys
import formatters


__author__ = 'Majid Garmaroudi'
__version__ = '0.0.1'
__license__ = 'MIT'

ignoreFiles = [".DS_Store", ".gitignore"]
path = ''


def getFilesPath(location, ignore):
    filesArray = []
    for path, subdirs, files in os.walk(location):
        for name in files:
            if len(ignore) >= 0 and path.find(ignore) >= 0:
                continue
            if name in ignoreFiles:
                continue

            filesArray.append(os.path.join(path, name))

    return filesArray


def getDate(path, file):
    repo = Repo(path)
    commit = repo.git.log("-1 --format=%cd", file)
    if len(commit) > 1:
        return commit.split('\n')[2][5:].strip()
    else:
        return None


def getGit(path, files):
    results = {}
    count = 0
    for file in files:
        reg = '^%s/' % path
        fileRelPath = re.sub(reg, '', file)
        date = getDate(path, fileRelPath)

        if date is not None and date != "":
            results[fileRelPath] = date

    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='List of last modified file(s) date')
    parser.add_argument('-g', '--git', help='Check git for file versions')
    parser.add_argument('-f', '--file', help='File(s) to be checked')
    parser.add_argument('-t', '--type', help='File(s) type')
    parser.add_argument('--format', help='Output Format - console or json')
    parser.add_argument('--ignore', help='File(s) type')

    args = vars(parser.parse_args())

    if args['git']:
        files = {}
        path = args['git']

        files = getGit(path, getFilesPath(path, '.git'))

        output_format = 'json'
        if args['format']:
            output_format = args['format']

        print formatters.Formatter(output_format).format(files)
        sys.exit()

    print "Nothing to do here!"
    sys.exit()
