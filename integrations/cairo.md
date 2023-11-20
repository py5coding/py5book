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

+++ {"editable": true, "slideshow": {"slide_type": ""}}

# Converting SVG Images with Cairo

[Cairo](https://www.cairographics.org/) is a widely used graphics library for
working with SVG images. Cairo is written in C but there are several Python
libraries available to make it accessible to py5.

Converting SVG Images to Py5Image objects with Cairo and
[](/reference/sketch_convert_shape) is useful to py5 users that want to use SVG
content in a Sketch that uses a rasterized renderer (such as the default JAVA2D
renderer or the OpenGL renderers P2D or P3D).

Processing can also load SVG images as Py5Shape objects with
[](/reference/sketch_load_shape) but they will load correctly if the SVG code
uses only a small subset of the full SVG specification. These limitations will
result in problems when loading SVG files created in sophisticated SVG editors
such as Inkscape or Adobe Illustrator.

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

Next you will need to install the Python libraries that py5 uses to access Cairo.

```bash
conda install --channel conda-forge cairosvg cairocffi
```

You can also install these with `pip`.

TODO: remove this from the install page

## Convert SVG Images

Let's start by importing the necessary libraries for this demonstration.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
from IPython.display import SVG

import py5_tools
import py5
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

Here is the SVG file we will be working with.

TODO: make my own SVG file in Inscape that breaks this load_shape(). Use fonts

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
with open('images/bot.svg') as f:
    svg_code = f.read()

SVG(svg_code)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

Now let's use that in our Sketch. Notice we are passing the SVG image path to
[](/reference/convert_image). It will load the SVG file, send it to Cairo for
rastorization, and return a `Py5Image` object.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def setup():
    py5.size(300, 300)

    svg = py5.convert_image('images/us_map.svg', scale=0.3, background_color='red')
    assert isinstance(svg, py5.Py5Image)

    py5.image(svg, 0, 0)
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
py5.run_sketch()
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

Here's what that looks like:

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
py5_tools.screenshot()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
import time

time.sleep(1)

py5.exit_sketch()
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

If instead we had tried to load the SVG file as a Py5Shape object with
[](/reference/sketch_load_shape), we would have seen this:

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def setup():
    py5.size(300, 300)

    svg = py5.load_shape('images/us_map.svg')

    py5.shape(svg, 0, 0)


py5.run_sketch()

py5_tools.screenshot()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
time.sleep(1)

py5.exit_sketch()
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

There are warnings, and it doesn't look as it should. Therefore, using [](/reference/convert_image) is a better option for working with this SVG image.

## Cairo Surfaces

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---

```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

| keyword argument | description |
|---|---|
| parent_width | width of parent container in pixels |
| parent_height | height of parent container in pixels |
| dpi | ratio between 1 inch and 1 pixel |
| scale | output_scaling factor |
| unsafe | resolve XML entities and allow very large files |
| background_color | background color to replace transparent background |
| negate_colors | negate SVG colors |
| invert_images | negate colors in embedded images |
| output_width | desired output width in pixels |
| output_height | desired output height in pixels |

+++ {"editable": true, "slideshow": {"slide_type": ""}}

```bash
conda install --channel conda-forge pycairo
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---

```
