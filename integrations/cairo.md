---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.7
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Converting SVG Images with Cairo

[Cairo](https://www.cairographics.org/) is a widely used graphics library for
working with SVG images. Cairo is written in C but there are several Python
libraries available to make it accessible to py5.

Converting SVG Images with Cairo is useful to py5 users that want to use SVG
content in a Sketch that uses a rasterized renderer (such as the default JAVA2D
renderer or the OpenGL renderers P2D or P3D). Processing and therefore py5's
ability to load SVG files as Py5Shape objects with
[](/reference/sketch_load_shape) is limited because Processing is not able to
interpret the full SVG specification syntax. This leads to aberrations in what
in the loaded Py5Shape object.

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

TODO: is this correct?
TODO: I should say which is installed for this example

You can also install these with `pip`.

There's no need to install more than one. While testing it seemed that
installing more than one caused problems.

TODO: remove this from the install page

## Convert SVG Images

Let's start by importing the necessary libraries for this demonstration.

```{code-cell} ipython3
from IPython.display import SVG

import py5_tools
import py5
```

Here is the SVG file we will be working with.

TODO: make my own SVG file in Inscape that breaks this load_shape(). Use fonts

```{code-cell} ipython3
with open('images/bot.svg') as f:
    svg_code = f.read()

SVG(svg_code)
```

Now let's use that in our Sketch. Notice we are passing the SVG image path to
[](/reference/convert_image). It will load the SVG file, send it to Cairo for
rastorization, and return a `Py5Image` object.

```{code-cell} ipython3
def setup():
    py5.size(300, 300)

    svg = py5.convert_image('images/us_map.svg')
    assert isinstance(svg, py5.Py5Image)

    py5.image(svg, 0, 0)
```

```{code-cell} ipython3
py5.run_sketch()
```

Here's what that looks like:

```{code-cell} ipython3
py5_tools.screenshot()
```

If instead we had tried to load the SVG file as a Py5Shape object with
[](/reference/sketch_load_shape), we would have seen this:

```{code-cell} ipython3
def setup():
    py5.size(300, 300)

    svg = py5.load_shape('images/us_map.svg')

    py5.shape(svg, 0, 0)


py5.run_sketch()

# TODO: screenshot() should consistently work here, it should pause and make sure
# drawing is complete

py5_tools.screenshot()
```

There are warnings, and it doesn't look as it should. Therefore, using [](/reference/convert_image) is a better option for working with this SVG image.

```{code-cell} ipython3

```
