---
jupytext:
  formats: ipynb,md:myst
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
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

# Custom Integrations

The methods [](/reference/sketch_convert_shape) and [](/reference/sketch_convert_image)
are customizable. In addition to the built-in integrations, you can create new integrations
that the [](/reference/sketch_convert_shape) and [](/reference/sketch_convert_image) methods
will use to convert Python objects into objects that are compatible with py5.

This page documents how to create custom integrations for both methods. Both methods have
similar customization designs.

This page will explain the customization design in detail, but if you are going to build a
custom integration, it is recommended you also have a look at the source code for the built-in
[image](https://github.com/py5coding/py5generator/blob/main/py5_resources/py5_module/py5/image_conversion.py)
and [shape](https://github.com/py5coding/py5generator/blob/main/py5_resources/py5_module/py5/shape_conversion.py)
customizations for additional insight and examples. You can also ask for help in
[GitHub Discussions](https://github.com/py5coding/py5generator/discussions).

Your custom integration will require you to create two functions. The first function is a
predicate function that accepts a Python object as its parameter and return True or False
to indicate if the object is convertable by your custom integration. The second function
must accept the same Python object and `**kwargs` parameters, and return an object compatible
with py5.

Your custom integrations will always take presidence over py5's builtin integrations.

We will begin with some imports needed for our examples.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
import numpy as np
from PIL import Image
from shapely import Point

import py5_tools
import py5
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## Custom Integrations for Image Conversion

For our image conversion example, we will create a custom integration that
converts PIL Image objects and by default rotates them 180 degrees. We will
also support a keyword argument to rotate the image by a different angle.

First we create our predicate function. It will simply check if an object is a PIL
Image object and return True or False. This function is identical to py5's built-in
customization for PIL Image objects.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def pillow_image_to_ndarray_precondition(obj):
    return isinstance(obj, Image.Image)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

The second function's parameters will be the object to be converted and `**kwargs` parameters.
It should not return a Py5Image object. Instead, it should either return a special
`NumpyImageArray` object or it should return the path to an image saved to disk that can
be read and loaded by py5.

The `NumpyImageArray` class is a special class py5 uses internally to manage image data in
numpy arrays. When creating an instance of `NumpyImageArray`, the first parameter should be
the numpy array with three dimensions. The first two dimensions should be the image's vertical
and horizontal dimensions, respectively. The third should be the image's color channels.

The second parameter should be a string indicating the color channel sequence of the
array's third dimension.  Any value that the [](/reference/sketch_create_image_from_numpy) method's
`bands` parameter accepts is acceptable here. If the color channel sequence is `L`, the array's
third dimension is optional.

If it is more convenient, your code can save the converted image to disk in a temporary file.
The Python library [tempfile](https://docs.python.org/3/library/tempfile.html) can help with
this.

The below conversion function is very similar to py5's built-in customization for PIL Image
objects.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def pillow_image_to_ndarray_converter(img, **kwargs):
    rotate = kwargs.get('rotate', 180)
    if img.mode not in ["RGB", "RGBA"]:
        img = img.convert(mode="RGB")
    img = img.rotate(rotate)
    return py5.NumpyImageArray(np.asarray(img), img.mode)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

The last step is to register the pair of functions with py5. After
registering, when the [](/reference/sketch_convert_image) method is
called, it will use this new conversion function we wrote to convert
PIL Image objects.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
py5.register_image_conversion(
    pillow_image_to_ndarray_precondition, pillow_image_to_ndarray_converter
)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

Now that everything is configured correctly,  let's create a Sketch
that uses our new PIL image conversion functionality.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def setup():
    py5.size(300, 300)

    pil_img = Image.open('images/rockies.jpg')
    img1 = py5.convert_image(pil_img)
    img2 = py5.convert_image(pil_img, rotate=45)
    py5.image(img1, 25, 100)
    py5.image(img2, 175, 100)
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
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

The result looks as we would expect. The left image is upside down
and the right image is rotated 45 degrees.

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

## Custom Integrations for Shape Conversion

For our shape conversion example, we will create a custom integration that
converts shapely Point objects into clouds of gaussian distributed points.
We will support keyword arguments for the standard deviation and count of
the points in the cloud.

First we create our predicate function. It will check if an object is a shapely
Point object and return True or False.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def shapely_point_precondition(obj):
    return isinstance(obj, Point)
```

The second function's parameters will be a sketch instance, the object to be converted,
and `**kwargs` parameters. The conversion function must return a new Py5Shape object
to be returned by [](/reference/sketch_convert_shape).

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def shapely_point_converter(sketch, obj, **kwargs):
    count = kwargs.get('count', 2500)
    stdev = kwargs.get('stdev', 25)
    points = stdev * np.random.randn(count, 2) + [obj.x, obj.y]

    s = sketch.create_shape()
    with s.begin_shape(sketch.POINTS):
        s.vertices(points)

    return s
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

We again register the pair of functions with py5. When
the [](/reference/sketch_convert_shape) method is called, it will
use the conversion function we wrote to convert shapely
Point objects.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
py5.register_shape_conversion(
    shapely_point_precondition, shapely_point_converter
)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

Now let's create a Sketch that uses our shapely Point conversion functionality.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def setup():
    py5.size(300, 300)

    point1 = Point(130, 210)
    point2 = Point(210, 130)

    points1 = py5.convert_shape(point1)
    points2 = py5.convert_shape(point2, count=5000, stdev=10)
    py5.shape(points1)
    py5.shape(points2)
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
py5.run_sketch()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
time.sleep(1)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

As expected, each point is rendered as a scattered field of individual points.

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

## Share Your Custom Integration Ideas!

The Python ecosystem is vast, and we are always on the lookout
for Python libraries we aren't familiar with that can further
enhance py5's capabilities. If you know of a Python library
that you think would be a good fit, please let us know in
[GitHub Discussions](https://github.com/py5coding/py5generator/discussions)
or elsewhere on Social Media.

```{code-cell} ipython3

```
