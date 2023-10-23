---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 2D Shapes and Shapely

[Shapely](https://shapely.readthedocs.io/) is a well-known and well-maintained
library for working with 2D geometry. Internally it is using the C/C++ library
[GEOS](https://libgeos.org/), commonly used for geographic information systems
(GIS) software.

## Setup

Install shapely with pip or with conda using the conda-forge channel.

```bash
pip install shapely
```

```bash
conda install shapely --channel conda-forge
```

Refer to [Shapely Installation page](https://shapely.readthedocs.io/en/stable/installation.html)
for more information.

Pro tip: DO NOT install Shapely from the default conda channel. You may end up
with an older version of the GEOS library and then frustrate yourself with bugs.

Development of py5's integration code was done with Shapely version 2.0.
The previous version, 1.8, should work just as well though.

## Convert Shapely objects to Py5Shape objects

Basic idea

Converted shape adapts the py5 drawing style in effect when `convert_shape()` is
called.

## Options

Explain two coordinate systems

Options - flip y, lines allow fills
change flip y default option???
