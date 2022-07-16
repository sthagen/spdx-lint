# -*- coding: utf-8 -*-
import copy
import json
import pathlib

import spdx_lint.lint as spl

EXAMPLES_PATH = pathlib.Path('examples')
EMPTY_JSON_OBJECT_PATH = pathlib.Path(EXAMPLES_PATH, 'empty_object.json')

SPDX_TYPICAL_JSON_2_2_PATH = pathlib.Path(EXAMPLES_PATH, 'spdx-v2.2_sbom.json')


def test_spdx_validation_nok_of_json_empty_object():
    with open(EMPTY_JSON_OBJECT_PATH, 'rt') as handle:
        sbom_doc = json.load(handle)
    assert spl.spdx_dci_is_valid(sbom_doc) is False


def test_spdx_validation_ok_of_typical_json_documentt(capsys):
    with open(SPDX_TYPICAL_JSON_2_2_PATH, 'rt') as handle:
        sbom_doc = json.load(handle)
    assert spl.spdx_dci_is_valid(sbom_doc) is True
    out, _ = capsys.readouterr()
    assert not out.strip()


def test_spdx_validation_nok_of_json_object_lacking_one_key():
    keys = tuple(spl.SPDX_2_2_DCI_JSON.keys())
    for key in keys:
        lacking = copy.deepcopy(spl.SPDX_2_2_DCI_JSON)
        del lacking[key]
        assert spl.spdx_dci_is_valid(lacking) is False
