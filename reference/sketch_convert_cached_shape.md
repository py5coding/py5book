# convert_cached_shape()

Convert non-py5 shape objects into Py5Shape objects, but cache the results.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
from shapely import Polygon, affinity


poly1 = Polygon([(0, 0), (0, 40), (40, 40), (40, 0)])
poly2 = affinity.translate(poly1, 20, 20)
shapely_shape = poly1.union(poly2)


def setup():
    py5.size(200, 200)
    py5.stroke_weight(5)


def draw():
    py5.background(204)
    py5_shape = py5.convert_cached_shape(shapely_shape)
    py5.shape(py5_shape, py5.mouse_x, py5.mouse_y)
```

</div></div>

</div>

## Description

Convert non-py5 shape objects into Py5Shape objects, but cache the results. This method is similar to [](sketch_convert_shape) with the addition of an object cache. Both methods facilitate py5 compatibility with other commonly used Python libraries.

See [](sketch_convert_shape) for method details.

Converting objects to Py5Shape objects can sometimes be slow. Usually you will not want to repeatedly convert the same object in your `draw()` function. Writing code to convert an object one time in `setup()` (with a `global` directive) to be later used in your `draw()` function can be a bit tedious. This method lets you write simpler code.

Your object must be hashable for object caching to work. If your object is not hashable, it cannot be cached and you will receive a warning. If you want py5 to ignore a previously cached object and force a re-conversion, set the `force_conversion` parameter to `True`.

## Signatures

```python
convert_cached_shape(
    obj: Any,  # object to convert into a Py5Shape object
    force_conversion: bool = False,  # force conversion of object if it is already in the cache
    **kwargs: dict[str, Any]
) -> Py5Shape
```

Updated on June 14, 2024 01:52:20am UTC
