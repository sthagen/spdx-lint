#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Visit folder tree with SPDX documents, validate the latter, and generate reports."""
import sys

import spdx_lint.lint as spdx_lint


def main(argv=None):
    """Process the job."""
    argv = sys.argv[1:] if argv is None else argv
    spdx_lint.main(argv)
