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

how to register new customization methods

Ask for ideas

```python

```

```python
import numpy as np
from PIL import Image
from shapely import Point

import py5_tools
import py5
```

## Custom Image Convertion Integrations

```python

```

```python
def pillow_image_to_ndarray_precondition(obj):
    return isinstance(obj, Image.Image)
```

```python
def pillow_image_to_ndarray_converter(img, **kwargs):
    rotate = kwargs.get('rotate', 180)
    if img.mode not in ["RGB", "RGBA"]:
        img = img.convert(mode="RGB")
    img = img.rotate(rotate)
    return py5.NumpyImageArray(np.asarray(img), img.mode)
```

```python
py5.register_image_conversion(
    pillow_image_to_ndarray_precondition, pillow_image_to_ndarray_converter
)
```

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

```python
py5_tools.screenshot()
```

```python
time.sleep(0.5)
py5.exit_sketch()
time.sleep(0.5)
```

```python

```

## Custom Shape Convertion Integrations

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

```python
py5.register_shape_conversion(
    shapely_point_precondition, shapely_point_converter
)
```

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

```python
py5_tools.screenshot()
```

```python
time.sleep(0.5)
py5.exit_sketch()
time.sleep(0.5)
```

```python

```
