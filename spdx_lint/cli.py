#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Visit folder tree with SPDX documents, validate the latter, and generate reports."""
import os
import sys

import spdx_lint.lint as spdx_lint


# pylint: disable=expression-not-assigned
def main(argv=None):
    """Process the job."""
    argv = sys.argv[1:] if argv is None else argv
    spdx_lint.main(argv)
 
