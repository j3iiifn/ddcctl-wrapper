# ddcctl-wrapper
A wrapper script for [ddcctl](https://github.com/kfix/ddcctl)

## Requirements
- Python3.7
- PyYAML

## Installation
```
% git clone https://github.com/j3iiifn/ddcctl-wrapper.git
% cd ddcctl-wrapper
% python3 -m venv venv
% source venv/bin/activate
(venv) % pip install -r requirements.txt
```

## Configuration
Format

```
mode 1:
    name or serial of display A:
        brightness: 99
        contrast: 99
    name or serial of display B:
        brightness: 88
        contrast: 88
mode 2:
    name or serial of display A:
        brightness: 99
        contrast: 99
```

Sample

```
morning:
  DELL P2214H:
    brightness: 0
    contrast: 48
  S221HQL:
    brightness: 10
    contrast: 100
afternoon:
  DELL P2214H:
    brightness: 0
    contrast: 45
  S221HQL:
    brightness: 0
    contrast: 80
evening:
  DELL P2214H:
    brightness: 0
    contrast: 32
  S221HQL:
    brightness: 0
    contrast: 50
```

## Usage
```
% bash ddcctl-wrapper.sh --help
usage: ddcctl-wrapper.py [-h] [-c CONFIG] (-m MODE | -l)

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        path to config yaml file
  -m MODE, --mode MODE
  -l, --list            print external displays list
```

## Example
Print a list of external displays.

```
% bash ddcctl-wrapper.sh -l
#1: serial = "3JY1P4C9178B", name = "DELL P2214H"
#2: serial = "LP20D0028536", name = "S221HQL"
```

Set brightness/contrast to external displays.

```
% bash ddcctl-wrapper.sh -m afternoon
DELL P2214H > brightness => 0
DELL P2214H > contrast => 45
S221HQL > brightness => 0
S221HQL > contrast => 80
```
