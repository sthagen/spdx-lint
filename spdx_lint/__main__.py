# -*- coding: utf-8 -*-
import sys

from spdx_lint.cli import main

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))  # pragma: no cover
