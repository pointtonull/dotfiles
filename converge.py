#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

import operator
import os
import shutil
import sys
import time
from collections import defaultdict
from contextlib import contextmanager
from os import path
from pathlib import Path
from subprocess import Popen, PIPE, check_output

CONVERGE_FILE = path.expanduser(".converge")


class Patterns:

    def __init__(self, configfile):
        for line in open(configfile):
            print(line)

@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)


def pull():
    proc = Popen("git pull --all", shell=True)
    proc.communicate()


def get_branch():
    """
    Returns current branch
    """
    command = "git rev-parse --abbrev-ref HEAD"
    branch = check_output(command, shell=True).decode().strip()
    return branch


def get_diff_files(branch):
    options = " ".join((
        "--name-status",
        "--diff-filter=ad",
    ))
    command = f"git diff {options} HEAD..{branch}"
    stdout = check_output(command, shell=True)
    return stdout.decode()


def vimdiff(left, right):
    command = f"vimdiff '{left}' '{right}'"
    print(command)
#     proc = Popen(command, shell=True)
#     proc.wait()


def main():

    this_branch = get_branch()
    with cd(".diverging/"):
        diverging_branch = get_branch()
        pull()
    pull()
    print(f"{this_branch} <- {diverging_branch}")

    diff_files = get_diff_files(diverging_branch)
#     patterns = Patterns(CONVERGE_FILE)

    left_dir = Path("./")
    right_dir = Path(".diverging")
    for status_file in diff_files.splitlines(): 
        try:
            status, filename = status_file.split("\t") 
        except ValueError:
            print(f"Could not process: {status_file}")

        filename = filename.rstrip("\n") 
        vimdiff(left_dir/filename, right_dir/filename)
    return



if __name__ == "__main__":
    main()

