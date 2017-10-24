import subprocess as sp
import sys
import time
import string
import os


def call(cmdline):
    child = sp.Popen(cmdline.split(), stdout= sp.PIPE)
    output, stderr = child.communicate('')
    return output
