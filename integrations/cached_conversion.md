---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.3
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

+++ {"editable": true, "slideshow": {"slide_type": ""}}

# Cached Conversion

When using py5 integrations along with [](/reference/sketch_convert_shape) or [](/reference/sketch_convert_image), you will often find yourself writing code that looks like this:

```{code-cell} ipython3
import py5

from trimesh.primitives import Sphere

trimesh_sphere = Sphere(100, subdivisions=2)
y_rot = 0
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def setup():
    global sphere
    py5.size(500, 500, py5.P3D)
    # convert trimesh sphere to Py5Shape object one time in setup()
    sphere = py5.convert_shape(trimesh_sphere)


def draw():
    global y_rot
    y_rot += 0.01

    py5.background("gray")
    py5.translate(py5.width / 2, py5.height / 2)
    py5.rotate_y(y_rot)
    # use the converted trimesh sphere in draw()
    py5.shape(sphere)


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

time.sleep(0.5)
py5.exit_sketch()
time.sleep(0.5)
```

It is a bit tedious to write that `global` statement and object conversion in `setup()`. To simplify the Sketch, you might be tempted to move the [](/reference/sketch_convert_shape) call to the `draw()` function, like this:

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def setup():
    py5.size(500, 500, py5.P3D)


def draw():
    global y_rot
    y_rot += 0.01

    py5.background("gray")
    py5.translate(py5.width / 2, py5.height / 2)
    py5.rotate_y(y_rot)
    # repeatedly convert trimesh sphere to Py5Shape object in draw()
    py5.shape(py5.convert_shape(trimesh_sphere))


py5.run_sketch()
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

Less typing, but the problem with this is that object conversion will be done repeatedly in the `draw()` function, potentially making the Sketch run slowly. It doesn't make that much of a difference in this simple example. For more complex Sketches with multiple object conversions, it will be noticeable.

As an alternative, you can use the [](/reference/sketch_convert_cached_shape) or [](/reference/sketch_convert_cached_image) methods. These methods do the same conversion as [](/reference/sketch_convert_shape) or [](/reference/sketch_convert_image), with the addition of caching functionality. This provides better Sketch performance. Both methods cache the results of the conversion and will retrieve converted objects on subsequent calls. Using these methods, you can write code that looks like this:

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def setup():
    py5.size(500, 500, py5.P3D)


def draw():
    global y_rot
    y_rot += 0.01

    py5.background("gray")
    py5.translate(py5.width / 2, py5.height / 2)
    py5.rotate_y(y_rot)
    # convert trimesh sphere to Py5Shape object one time in draw()
    py5.shape(py5.convert_cached_shape(trimesh_sphere))


py5.run_sketch()
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

The caching functionality only works if the converted objects are "hashable". Bottom line, it must be possible to use the object you pass to [](/reference/sketch_convert_shape) or [](/reference/sketch_convert_image) as the key of a dictionary. For the Python libraries relevant to py5 object conversion, only PIL Image objects are not hashable and have this limitation. You would see a warning message reminding you of this if you were to pass a PIL Image object with [](/reference/sketch_convert_cached_image).
