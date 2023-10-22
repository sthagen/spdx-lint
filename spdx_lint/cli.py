"""Visit folder tree with SPDX documents, validate the latter, and generate reports."""
import sys
from typing import no_type_check

import spdx_lint.lint as spdx_lint


@no_type_check
def main(argv=None):
    """Process the job."""
    argv = sys.argv[1:] if argv is None else argv
    spdx_lint.main(argv)
