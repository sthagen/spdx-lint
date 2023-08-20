# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/spdx-lint/blob/default/sbom/cdx.json) with SHA256 checksum ([9d35a1d5 ...](https://git.sr.ht/~sthagen/spdx-lint/blob/default/sbom/cdx.json.sha256 "sha256:9d35a1d5fe00f85739c0abef46f1711dd49384fc9e8614375ccf34efd96b42be")).
<!--[[[end]]] (checksum: dfe600cfcc9ae578db9aca894000101e)-->
## Licenses

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                            | Version                                                | License     | Author            | Description (from packaging data)                                  |
|:----------------------------------------------------------------|:-------------------------------------------------------|:------------|:------------------|:-------------------------------------------------------------------|
| [jsonschema](https://github.com/python-jsonschema/jsonschema)   | [4.19.0](https://pypi.org/project/jsonschema/4.19.0/)  | MIT License | Julian Berman     | An implementation of JSON Schema validation for Python             |
| [referencing](https://github.com/python-jsonschema/referencing) | [0.30.2](https://pypi.org/project/referencing/0.30.2/) | MIT License | Julian Berman     | JSON Referencing + Python                                          |
| [typer](https://github.com/tiangolo/typer)                      | [0.9.0](https://pypi.org/project/typer/0.9.0/)         | MIT License | Sebastián Ramírez | Typer, build great CLIs. Easy to code. Based on Python type hints. |
| [xmlschema](https://github.com/sissaschool/xmlschema)           | [2.4.0](https://pypi.org/project/xmlschema/2.4.0/)     | MIT License | Davide Brunato    | An XML Schema validator and decoder                                |
<!--[[[end]]] (checksum: 60bf34b4b3e2be81abca5760ac5554d8)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                      | Version                                              | License     | Author                     | Description (from packaging data)                                    |
|:----------------------------------------------------------|:-----------------------------------------------------|:------------|:---------------------------|:---------------------------------------------------------------------|
| [attrs](https://www.attrs.org/en/stable/changelog.html)   | [23.1.0](https://pypi.org/project/attrs/23.1.0/)     | MIT License | Hynek Schlawack <hs@ox.cx> | Classes Without Boilerplate                                          |
| [click](https://palletsprojects.com/p/click/)             | [8.1.6](https://pypi.org/project/click/8.1.6/)       | BSD License | UNKNOWN                    | Composable command line interface toolkit                            |
| [elementpath](https://github.com/sissaschool/elementpath) | [4.1.5](https://pypi.org/project/elementpath/4.1.5/) | MIT License | Davide Brunato             | XPath 1.0/2.0/3.0/3.1 parsers and selectors for ElementTree and lxml |
<!--[[[end]]] (checksum: 657ca67fe3e513c2534e5031ba7cd849)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
jsonschema==4.19.0
├── attrs [required: >=22.2.0, installed: 23.1.0]
├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.7.1]
│   └── referencing [required: >=0.28.0, installed: 0.30.2]
│       ├── attrs [required: >=22.2.0, installed: 23.1.0]
│       └── rpds-py [required: >=0.7.0, installed: 0.9.2]
├── referencing [required: >=0.28.4, installed: 0.30.2]
│   ├── attrs [required: >=22.2.0, installed: 23.1.0]
│   └── rpds-py [required: >=0.7.0, installed: 0.9.2]
└── rpds-py [required: >=0.7.1, installed: 0.9.2]
typer==0.9.0
├── click [required: >=7.1.1,<9.0.0, installed: 8.1.6]
└── typing-extensions [required: >=3.7.4.3, installed: 4.7.1]
xmlschema==2.4.0
└── elementpath [required: >=4.1.5,<5.0.0, installed: 4.1.5]
````
<!--[[[end]]] (checksum: 2e05468ee1c2fd604243428f44411a36)-->
