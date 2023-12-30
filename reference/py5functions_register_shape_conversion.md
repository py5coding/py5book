# register_shape_conversion()

Register new shape conversion functionality to be used by [](sketch_convert_shape).

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for register_shape_conversion()](/images/reference/Py5Functions_register_shape_conversion_0.png)

</div><div class="example-cell-code">

```python
import numpy as np
from shapely import Point

def shapely_point_precondition(obj):
    return isinstance(obj, Point)

# draw shapely points as a group of gaussian distributed points
def shapely_point_converter(sketch, obj, **kwargs):
    sigma = kwargs.get('sigma', 5)
    points = sigma * np.random.randn(1000, 2) + [obj.x, obj.y]

    s = sketch.create_shape()
    with s.begin_shape(sketch.POINTS):
        s.vertices(points)

    return s

py5.register_shape_conversion(
    shapely_point_precondition, shapely_point_converter
)

def setup():
    point1 = Point(30, 70)
    point2 = Point(70, 30)

    points1 = py5.convert_shape(point1)
    points2 = py5.convert_shape(point2, sigma=10)
    py5.println(type(points1))
    py5.println(type(points2))
    py5.shape(points1)
    py5.shape(points2)
```

</div></div>

</div>

## Description

Register new shape conversion functionality to be used by [](sketch_convert_shape).  This will allow users to extend py5's capabilities and compatability within the Python ecosystem.

The `precondition` parameter must be a function that accepts an object as a parameter and returns `True` if and only if the `convert_function` can successfully convert the object.

The `convert_function` parameter must be a function that accepts an object as a parameter and returns a [](py5shape) object.

## Signatures

```python
register_shape_conversion(
    precondition: Callable,  # predicate determining if an object can be converted
    convert_function: Callable,  # function to convert object to Py5Shape object
) -> None
```

Updated on December 11, 2023 16:58:45pm UTC
