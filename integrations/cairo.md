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

# Converting SVG Images with Cairo

[Cairo](https://www.cairographics.org/) is a widely used graphics library for
working with SVG images. Cairo is written in C but there are several Python
libraries available to make it accessible to py5.

## Setup

First you must install the 2D graphics library Cairo. The easiest way to do this
is with conda using the conda-forge channel. This will work for any operating
system.

```bash
conda install cairo --channel conda-forge
```

If you don't want to use conda, refer to the install instructions in the [Cairo
documentation](https://www.cairographics.org/download/). Installing Cairo on
Windows without conda is challenging.

Next you will need to install a Python library that uses Cairo. Pick one (1) of
the following options:

```
conda install --channel conda-forge cairosvg
conda install --channel conda-forge pycairo
conda install --channel conda-forge cairocffi
```

You can also install these with `pip`.

There's no need to install more than one. While testing it seemed that
installing more than one caused problems.

TODO: remove this from the install page

## Convert SVG images to Py5Image objects
