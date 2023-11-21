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

# SVG Images and Cairo

[Cairo](https://www.cairographics.org/) is a widely used graphics library for
working with SVG (Scalable Vector Graphics) images. Cairo is written in C but
there are several Python libraries available to make it accessible to py5.

Converting SVG Images to Py5Image objects with the
[](/reference/sketch_convert_image) method is useful to py5 users that want to
use SVG content in a Sketch that uses a rasterized renderer (such as the default
JAVA2D renderer or the OpenGL renderers P2D or P3D).

Processing and therefore py5 can load SVG images as Py5Shape objects with
[](/reference/sketch_load_shape) but the method supports only a small subset of
the full SVG specification. Processing did not intend to provide a comprehensive
SVG interpreter, as implementing that functionality would be a significant
undertaking. Nevertheless, the method's limitations will frequently result in
problems when loading SVG files created in sophisticated SVG editors such as
[Inkscape](https://inkscape.org/) or Adobe Illustrator.

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

Next you will need to install the Python libraries that py5 uses to access Cairo
and work with SVG files. The [cairosvg](https://cairosvg.org/) library depends on
[cairocffi](https://doc.courtbouillon.org/cairocffi/stable/).

```bash
conda install --channel conda-forge cairosvg cairocffi
```

You can also install these with `pip`.

## Convert SVG Images

Let's start by importing the necessary libraries for this demonstration.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
from IPython.display import SVG
import numpy as np
import cairocffi

import py5_tools
import py5
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

Below is the SVG file we will be working with, created in Inkscape. Observe
the SVG image uses a color gradient and has centered text.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
with open('images/py5_is_awesome.svg') as f:
    svg_code = f.read()

SVG(svg_code)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

Now let's use this in a Sketch. Notice we are passing the SVG image path to
[](/reference/sketch_convert_image). It will read the SVG file, and then the cairosvg
library will send it to Cairo for rastorization via cairocffi. The method call
returns a `Py5Image` object.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def setup():
    py5.size(500, 500)

    svg = py5.convert_image('images/py5_is_awesome.svg')
    assert isinstance(svg, py5.Py5Image)

    py5.image(svg, 0, 0)


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
    py5.size(500, 500)

    svg = py5.load_shape('images/py5_is_awesome.svg')

    py5.shape(svg, 0, 0)


py5.run_sketch()
```

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
time.sleep(1)

py5.exit_sketch()
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

Not awesome. It can't handle the color gradient and the text alignment is wrong.
Therefore, using [](/reference/sketch_convert_image) is a better option for
working with this SVG image.

## Optional Conversion Parameters

The [](/reference/sketch_convert_image) method provides a few optional customization
parameters for the conversion of SVG images.

The most useful optional parameter is `scale`, allowing you to change the scale of
the converted SVG image. Another useful parameter is `negate_colors`, which will
invert the SVG's color palette.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def setup():
    py5.size(500, 500)

    svg1 = py5.convert_image('images/py5_is_awesome.svg', scale=0.5)
    svg2 = py5.convert_image('images/py5_is_awesome.svg', scale=0.5, negate_colors=True)

    py5.image(svg1, 0, 0)
    py5.image(svg2, 250, 0)
    py5.image(svg2, 0, 250)
    py5.image(svg1, 250, 250)


py5.run_sketch()
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

Here's the result:

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
time.sleep(1)

py5.exit_sketch()
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

The full list of optional parameters is below.

+++ {"editable": true, "slideshow": {"slide_type": ""}}

| keyword argument | description |
|---|---|
| parent_width | width of parent container in pixels |
| parent_height | height of parent container in pixels |
| dpi | ratio between 1 inch and 1 pixel |
| scale | output scaling factor |
| unsafe | resolve XML entities and allow very large files |
| background_color | background color to replace transparent background |
| negate_colors | negate SVG colors |
| invert_images | negate colors in embedded images |
| output_width | desired output width in pixels |
| output_height | desired output height in pixels |

## Cairo Drawing Surfaces

Next we will demonstrate py5's ability to support Cairo drawing Surfaces.
Drawing images with this is a bit tedious but perhaps someone will get good
use out of it. The drawing methods provided by py5 are generally easier to
use but this approach offers drawing techniques not available in py5. See the
[cairocffi documentation](https://doc.courtbouillon.org/cairocffi/stable/api.html)
for inspiration and ideas.

Below is a simple example to get you started.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def setup():
    py5.size(500, 500)

    surface = cairocffi.RecordingSurface(cairocffi.CONTENT_COLOR_ALPHA, (0, 0, 500, 500))
    context = cairocffi.Context(surface)
    context.scale(500, 500)

    context.set_line_width(0.1)
    context.move_to(0.1, 0.5)
    context.curve_to(0.4, 0.9, 0.6, 0.1, 0.9, 0.5)
    context.stroke()

    context.set_source_rgba(1, 0.1, 0.1, 0.5)
    context.set_line_width(0.01)
    for y in np.linspace(0, 1, num=20):
        context.move_to(0, y)
        context.line_to(1, y)
    context.stroke()
    
    cairo_surface = py5.convert_image(surface)
    py5.image(cairo_surface, 0, 0)


py5.run_sketch()
```

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
time.sleep(1)

py5.exit_sketch()
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## Pycairo

Alternatively, you can install [Pycairo](https://pycairo.readthedocs.io/en/latest/)
instead of cairocffi.

```bash
conda install --channel conda-forge pycairo
```

Cairocffi is designed to be a drop-in replacement to Pycairo, so Pycairo can be used
just like cairocffi in the previous example.

Do not install both Pycairo and cairocffi in the same Python environment, as this
seems to cause problems. Removing cairocffi means removing cairosvg and py5's
ability to convert SVG files to `Py5Image` objects. For most users, installing
cairocffi and cairosvg is the best choice.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---

```
