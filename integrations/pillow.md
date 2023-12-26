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

# Images and Pillow

[Pillow](https://pillow.readthedocs.io/en/stable/) is a popular Python library for working with images. It is a friendly fork of a similar library called PIL.

Pillow is one of py5's dependencies, so it will always be installed alongside py5.

Internally, py5 uses Pillow to save frames. This enables py5 to save images in a wide variety of image formats, beyond what Processing supports.

Py5's [](/reference/sketch_convert_shape) method enables py5 users to load images in any format Pillow supports and to convert them in to `Py5Image` objects.

Let's experiment with the Pillow image library and py5, starting with the imports.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
from PIL import Image

import py5_tools
import py5
```

## Basic Image Example

First we will load an image.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
logo = Image.open('images/logo.png')

logo
```

We can then use this Pillow image in our Sketch.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def setup():
    py5.size(400, 400)
    py5.background(64)
    py5.image_mode(py5.CENTER)

    img = py5.convert_image(logo)    
    py5.image(img, 200, 200)


py5.run_sketch()
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
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

It looks very much like what you'd expect.

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
time.sleep(0.5)
py5.exit_sketch()
time.sleep(0.5)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

Converting a Pillow image to a `Py5Image` object takes a small amount of time to complete but if you want to repeatedly draw your Pillow image to the screen, it is recommended that you do the conversion once in `setup()`. You can do this with the `global` keyword. For example:

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def setup():
    global img
    py5.size(400, 400)
    py5.background(64)
    py5.image_mode(py5.CENTER)

    img = py5.convert_image(logo)


def draw():
    xval = py5.random(py5.width)
    yval = py5.random(py5.height)
    py5.image(img, xval, yval)


py5.run_sketch()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
time.sleep(3)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

And here's what that looks like.

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
time.sleep(0.5)
py5.exit_sketch()
time.sleep(0.5)
```
