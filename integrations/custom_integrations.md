---
jupyter:
  jupytext:
    cell_metadata_filter: -all
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.7
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

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
customizations for additional examples. You can also ask for help in
[GitHub Discussions](https://github.com/py5coding/py5generator/discussions).

Your custom integration will require two functions. The first function is a predicate function
that accepts a Python object as its parameter and return True or False to indicate if the object
is convertable by your custom integration. The second function must accept the same Python
object and `**kwargs` parameters, and return an object compatible with py5.

Your custom integrations will always take presidence over the builtin integrations.

We will begin with some imports needed for our examples.

```python
import numpy as np
from PIL import Image
from shapely import Point

import py5_tools
import py5
```

## Custom Integrations for Image Conversion


As an example, we will create a custom integration that converts PIL Image objects
and by default rotates them 180 degrees. We will also support a keyword argument
to rotate the image by a different angle.

First we create our predicate function. It will simply check if an object is a PIL
Image object and return True or False. This function is identical to py5's built-in
customization for PIL Image objects.

```python
def pillow_image_to_ndarray_precondition(obj):
    return isinstance(obj, Image.Image)
```

The second function's parameters will be the object to be converted and `**kwargs` parameters.
It should not return a Py5Image object. Instead, it should return a special `NumpyImageArray`
object or it should return the path to an image saved to disk that can be read and loaded by
py5.

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

```python
def pillow_image_to_ndarray_converter(img, **kwargs):
    rotate = kwargs.get('rotate', 180)
    if img.mode not in ["RGB", "RGBA"]:
        img = img.convert(mode="RGB")
    img = img.rotate(rotate)
    return py5.NumpyImageArray(np.asarray(img), img.mode)
```

The last step is to register the pair of functions with py5. After
registering, when the [](/reference/sketch_convert_image) method is
called, it will use the conversion function we wrote to convert PIL
Image objects.

```python
py5.register_image_conversion(
    pillow_image_to_ndarray_precondition, pillow_image_to_ndarray_converter
)
```

Now that everything is configured correctly,  let's create a Sketch
that uses our new PIL image conversion functionality.

```python
def setup():
    pil_img = Image.open('images/rockies.jpg').reduce(2)
    img1 = py5.convert_image(pil_img)
    img2 = py5.convert_image(pil_img, rotate=45)
    py5.image(img1, 0, 25)
    py5.image(img2, 50, 25)
```

```python
py5.run_sketch()
```

```python
import time

time.sleep(1)
```

The result looks as we would expect. The left image is upside down
and the right image is rotated 45 degrees.

```python
py5_tools.screenshot()
```

```python
time.sleep(0.5)
py5.exit_sketch()
time.sleep(0.5)
```

## Custom Integrations for Shape Conversion

```python

```

```python
def shapely_point_precondition(obj):
    return isinstance(obj, Point)
```

```python
# draw shapely points as a group of gaussian distributed points
def shapely_point_converter(sketch, obj, **kwargs):
    sigma = kwargs.get('sigma', 5)
    points = sigma * np.random.randn(1000, 2) + [obj.x, obj.y]

    s = sketch.create_shape()
    with s.begin_shape(sketch.POINTS):
        s.vertices(points)

    return s
```

We again register the pair of functions with py5. When
the [](/reference/sketch_convert_shape) method is called, it will
use the conversion function we wrote to convert shapely
Point objects.

```python
py5.register_shape_conversion(
    shapely_point_precondition, shapely_point_converter
)
```

Now let's create a Sketch that uses our shapely Point conversion functionality.

```python
def setup():
    point1 = Point(30, 70)
    point2 = Point(70, 30)

    points1 = py5.convert_shape(point1)
    points2 = py5.convert_shape(point2, sigma=10)
    py5.shape(points1)
    py5.shape(points2)
```

```python
py5.run_sketch()
```

```python
time.sleep(1)
```

As expected, each point is rendered as a scattered field of individual points.

```python
py5_tools.screenshot()
```

```python
time.sleep(0.5)
py5.exit_sketch()
time.sleep(0.5)
```

## Share Your Ideas!



```python

```
