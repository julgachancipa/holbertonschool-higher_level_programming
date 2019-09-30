#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: {:s}\n".format(str(e)))
        return None
    return result
