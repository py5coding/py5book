# convert_shape()

Convert non-py5 shape objects into Py5Shape objects.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for convert_shape()](/images/reference/Sketch_convert_shape_0.png)

</div><div class="example-cell-code">

```python
from shapely import Polygon, affinity


def setup():
    py5.stroke_weight(5)

    poly1 = Polygon([(0, 0), (0, 40), (40, 40), (40, 0)])
    poly2 = affinity.translate(poly1, 20, 20)

    shapely_shape = poly1.union(poly2)
    py5_shape = py5.convert_shape(shapely_shape)
    py5.shape(py5_shape, 20, 20)
```

</div></div>

</div>

## Description

Convert non-py5 shape objects into Py5Shape objects. This facilitates py5 compatability with other commonly used Python libraries.

This method is comparable to [](sketch_load_shape), except instead of reading shape files from disk, it converts shape data from other Python objects.

Passed shape object types must be known to py5's shape conversion tools. New object types and functions to effect conversions can be registered with [](py5functions_register_shape_conversion).

The `convert_shape()` method has builtin support for the conversion of shapely and trimesh objects. This will allow users to explore the geometry capabilities of those libraries.

## Signatures

```python
convert_shape(
    obj: Any,  # object to convert into a Py5Shape object
    **kwargs: dict[str, Any]
) -> Py5Shape
```

Updated on October 06, 2023 13:36:04pm UTC
