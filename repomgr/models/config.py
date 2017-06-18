class _Cache:
    def __init__(self, filename: str):
        self.filename: str = filename


class _Logging:
    def __init__(self, filename: str, level: int):
        self.filename: str = filename
        self.level: int = level


class _System:
    def __init__(self, name: str, tag: str, path: str):
        self.name: str = name
        self.tag: str = tag
        self.path: str = path


class Config:
    def __init__(self, cache: _Cache, logging: _Logging, systems: [_System]):
        self.cache: _Cache = cache
        self.logging: _Logging = logging
        self.systems: [_System] = systems
