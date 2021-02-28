# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long

SPDX_2_2_DCI_TV = {
    "SPDXVersion": "SPDX-2.2",
    "DataLicense": "CC0-1.0",
    "SPDXID": "SPDXRef-DOCUMENT",
    "DocumentName": "$_SINGLE_LINE",
    "DocumentNamespace": "$_URI_MINUS_PART",
    "[ExternalDocumentRef]": [
        "DocumentRef-$_IDSTRING $_SPDX_DOCUMENT_URI $_PREFIX_COLON_CHECKSUM",
    ],
    "[LicenseListVersion]": "$_MAJOR.$_MINOR",
    "Creator": [
        "Person: $_PERSON_NAME [($_EMAIL)]",
        "Organization: $_ORGANIZATION [($_EMAIL)]",
        "Tool: $_TOOL_IDENTIFIED-$_VERSION",
    ],
    "Created": "%Y-%m-%dT%H:%M:%SZ",
    "[CreatorComment]": "<text>$_MULTI_LINE_TEXT</text>",
    "[DocumentComment]": "<text>$_MULTI_LINE_TEXT</text>",
}

SPDX_2_2_DCI_JSON = {  # Reversed engineered from round trip conversion - TODO(sthagen) later use json schema
    "SPDXID": "SPDXRef-DOCUMENT",
    "spdxVersion": "SPDX-2.2",
    "creationInfo": {
        "created": "%Y-%m-%dT%H:%M:%SZ",
        "creators": [
            "Person: $_PERSON_NAME [($_EMAIL)]",
            "Organization: $_ORGANIZATION [($_EMAIL)]",
            "Tool: $_TOOL_IDENTIFIED-$_VERSION",
        ]
    },
    "name": "$_SINGLE_LINE",
    "dataLicense": "CC0-1.0",
    "documentNamespace": "$_URI_MINUS_PART",

}


def spdx_dci_is_valid(sbom):
    """Shallow key level validation for DCI part of SPDX documents."""
    if not sbom:
        return False
    for key in SPDX_2_2_DCI_JSON.keys():
        if key.startswith("["):
            continue
        try:
            if not sbom.get(key):
                return False
        except AttributeError as e:
            print(str(sbom), e)  # TODO(sthagen) when I am a grown up, I want to really log

    return True
