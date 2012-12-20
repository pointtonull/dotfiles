#!/usr/bin/env python
#-*- coding: UTF-8 -*-

from subprocess import call, Popen, PIPE
import os
import shutil

SYSTEM_CONFIGFILE = "system.csv"
SYSTEM_DIR = "system/"
USER_CONFIGFILE = "user.csv"
USER_DIR = "user/"
VERBOSE = 0


def vcall(*args, **kwargs):
    """Verbose call. Print the command, execute, return exit code"""
    if VERBOSE:
        print(", ".join(args))
    try:
        error = call(*args, **kwargs)
    except OSError, e:
        print("Command failed: %s" % e)
        error = None
    return error


    if any((REMOTE in line for line in mounteds)):
        return True
    else:
        error = vcall("mount %s" % REMOTE, shell=True)
        if error == 0:
            return True
        else:
            return

def rsync(origen, destino):
    print("%s > %s" % (origen, destino))
    vcall('rsync -ar --no-owner --no-g --modify-window=5 --delete'
        ' "%s/" "%s"' % (origen, destino), shell=True)

def makedirs(path):
    try:
        os.makedirs(path)
    except OSError:
        pass


def main():
    for line in open(USER_CONFIGFILE):
        src, dst = line.strip().split(";")
        src = os.path.expanduser(src)
        dst = USER_DIR + dst
        if os.path.isfile(src):
            makedirs(os.path.realpath(dst + "/.."))
            shutil.copy(src, dst)
        else:
            makedirs(dst)
            rsync(src, dst)

        vcall('git add "%s"' % dst, shell=True)
#    vcall('git diff --name-only', shell=True)


if __name__ == "__main__":
    exit(main())
