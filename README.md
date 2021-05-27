## aaaa

[![Build Status](https://travis-ci.com/sgrieve/aaaa.svg?branch=master)](https://travis-ci.com/sgrieve/aaaa) [![Coverage](https://img.shields.io/codecov/c/github/sgrieve/aaaa)](https://codecov.io/gh/sgrieve/aaaa) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aaaa) ![PyPI - License](https://img.shields.io/pypi/l/aaaa)

Have you ever been creating an animated plot by saving a series of images and joining them together? The obvious way to name these frames would be using numbers:

```python
for i in range(15):
    plt.savefig('{}.png'.format(i))
```

But many operating systems will order these files as follows:

```bash
0.png
1.png
10.png
11.png
12.png
13.png
14.png
2.png
3.png
4.png
5.png
6.png
7.png
8.png
9.png
```

Thereby screwing up the order of your animation.

This is where `aaaa` (pronounced like a scream) comes in! `aaaa` has a single class which creates an iterator that yields an alphabetical sequence `aa`, `ab`, `ac`, etc. So we can change our above example:

```python
from aaaa import aaaa

fname = aaaa()

for i in range(15):
    plt.savefig('{}.png'.format(next(fname)))
```

Which will preserve the order of the files in your operating system:

```bash
aa.png
ab.png
ac.png
ad.png
ae.png
af.png
ag.png
ah.png
ai.png
aj.png
ak.png
al.png
am.png
an.png
ao.png
```

File sorting can differ between operating systems, sometimes with [serious results](https://arstechnica.com/information-technology/2019/10/chemists-discover-cross-platform-python-scripts-not-so-cross-platform/).


### Installation

`aaaa` has no dependences and is tested on Python 3.5 through 3.8 and it can be installed via pip:

```bash
pip install aaaa
```

### Usage

There are two ways to use `aaaa`. Firstly, you can loop directly over an `aaaa` instance, until there are no items left (in this case the last value of name will be `zz`):

```python
from aaaa import aaaa

names = aaaa()

for name in names:
    print(name)

```

Or, you can use the `next()` operator to only get as many values as you need:

```python
from aaaa import aaaa

names = aaaa()

for i in range(10):
    print(next(names))

```

The default length of an output from `aaaa` is 2 characters long - this will allow you to order 676 files. If you need a larger or smaller amount of characters you can specify this as an argument to `aaaa`:

```python
from aaaa import aaaa

names_short = aaaa(1)
names_long = aaaa(4)

print(next(names_short), next(names_long))
# Outputs --> a aaaa

```

Beyond four or five characters in length, initializing `aaaa` becomes prohibitively slow. Note that four characters gives you **456976** permutations - so you should never need more than this.


### Contribute

For my purposes this package is feature complete, but if you find a bug, or have a feature request, open an issue, or create a pull request!


### License

The project is licensed under the MIT license.
