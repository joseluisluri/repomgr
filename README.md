# repomgr - ROM handling utility
Command-line tool for handling ROM repository

## Introduction
Provides a high-level command-line interface for ROM managment:

> One tool to rule them all, one tool to find them.


Synopsis:
```
repomgr COMMAND [OPTIONS]
```
Dependencies:
- **pyyaml**: http://pyyaml.org
- **tabulate**: https://pypi.python.org/pypi/tabulate

Usage:
- **search** <u>regexp</u>: performs a full text search on ROM index cache for the specified seed.
- **info** <u>crc32</u>: display ROM information.
- **update**: synchronize the ROM index cache from their repo.


Examples:
```
$ repomgr search zelda
[4407c759] Legend of Zelda, The - Link's Awakening (Canada).gb - 512 KB
[bf2ab18b] Legend of Zelda, The - Link's Awakening (France).gb - 512 KB
[760ab4e7] Legend of Zelda, The - Link's Awakening (Germany).gb - 512 KB
[7d1b6cd6] Legend of Zelda, The - Link's Awakening (USA, Europe) (Rev A).gb - 512 KB
[34d08e7b] Legend of Zelda, The - Link's Awakening (USA, Europe) (Rev B).gb - 512 KB
[8cf27c90] Legend of Zelda, The - Link's Awakening (USA, Europe).gb - 512 KB
[ea20b82a] Zelda no Densetsu - Yume o Miru Shima (Japan) (Rev A).gb - 512 KB
[39a6684e] Zelda no Densetsu - Yume o Miru Shima (Japan).gb - 512 KB
```

Get 

```
$ repomgr info 4407c759
name: Legend of Zelda, The - Link's Awakening (Canada).gb
system: Nintendo - Game Boy
modified: 2010-08-19 22:42:30
size: 512 KB
crc32: 0x4407c759
```

Example of ROM index cache update:
```
$ repomgr update
Starting to update ROM index cache:
Atari - 5200 (107 roms)
Nintendo - Game Boy (1609 roms)
All done. :)
```

## Installation
The latest stable release can be installed using PyPi:
```
$ pip install repomgr
```

The unstable version must be installed from sources:
```
$ git clone https://github.com/joseluisluri/repomgr.git
$ cd repomgr
$ python setup.py install
```

## Configuration

*repomgr* looks in the current working directory for a config file.

**config.yml**:
```
cache:
  filename: cache.json
logging:
  filename: logging.log
  level: 10
systems:
  - name: Atari - 5200
    tag: atari-5200
    path: \\NAS-Drive\Roms\Atari - 5200
  - name: Nintendo - Game Boy
    tag: nintendo-game-body
    path: \\NAS-Drive\Roms\Nintendo - Game Boy
```

**Note:** logging.level - debug: 10, info: 20, warn: 30, error: 40, critical: 50

## ROM repository structure
Each system must be defined as a directory in order to store roms collection.

Example:
```
/
- Roms/
  - Atari - 5200/
    - Addams Family, The (World).zip
    - Aerial Assault (Japan) (Rev 1).zip
    - ...
  - Atari - 7800/
  - ...
```

## ROM compression
A rom must be compressed like this:
- **Format**: Zip
- **Extension**: *.zip
- **Compression level**: Normal

## Developers

```
$ git clone https://github.com/joseluisluri/repomgr.git
$ python3 setup.py sdist
$ python3 setup.py install
$ python3 repomgr -h
```

## License

Copyright (c) 2017 José Luis Luri. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY JOSÉ LUIS LURI ''AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those of the authors and should not be interpreted as representing official policies, either expressed or implied, of José Luis Luri.