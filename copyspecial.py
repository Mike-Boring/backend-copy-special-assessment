#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Mike Boring"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    special_paths_list = []
    pattern_match = '(\w+)__(\w+)__\.(\w+)'
    for file_name in os.listdir(dirname):
        if re.match(pattern_match, file_name):
            if file_name not in str(special_paths_list):
                special_paths_list.append(os.path.abspath(file_name))
        else:
            continue
    for special_path in special_paths_list:
        print(special_path)

    return special_paths_list


def copy_to(path_list, dest_dir):
    """Given a path list and destination dir, copies all files to destination."""
    os.makedirs(dest_dir)
    for path_name in path_list:
        shutil.copy(path_name, dest_dir)
    return


def zip_to(path_list, dest_zip):
    """Creates a zip file containing all files from list."""
    path_names = ''.join(path_list)
    print('path names: ', path_names)
    print('Command I am going to do: ' +
          'zip', '-j', dest_zip, path_list[0], path_list[1])
    subprocess.run(['zip', '-j', dest_zip, path_list[0], path_list[1]])
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions


if __name__ == "__main__":
    main(sys.argv[1:])
