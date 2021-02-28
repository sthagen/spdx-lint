# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import json
import pathlib
import pytest  # type: ignore

import spdx_lint.lint as spl

EXAMPLES_PATH = pathlib.Path("examples")
EMPTY_JSON_OBJECT_PATH = pathlib.Path(EXAMPLES_PATH, "empty_object.json")

SPDX_TYPICAL_JSON_2_2_PATH = pathlib.Path(EXAMPLES_PATH, "spdx-v2.2_sbom.json")


def test_spdx_validation_nok_of_json_empty_object():
    with open(EMPTY_JSON_OBJECT_PATH, "rt") as handle:
        sbom_doc = json.load(handle)
    assert spl.spdx_dci_is_valid(sbom_doc) is False
