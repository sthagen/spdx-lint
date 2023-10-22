# [[[fill git_describe()]]]
__version__ = '2023.10.22+parent.e8a57708'
# [[[end]]] (checksum: c71a81085241078e6697f1bfe3d3eb9c)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
