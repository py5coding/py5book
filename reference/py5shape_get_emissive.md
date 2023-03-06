# Py5Shape.get_emissive()

Get the emissive color setting for one of a `Py5Shape` object's vertices.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for get_emissive()](/images/reference/Py5Shape_get_emissive_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    py5.background(0)
    py5.directional_light(200, 200, 200, .5, 0, -1)
    py5.emissive(0, 50, 100)
    py5.no_stroke()
    s = py5.create_shape(py5.SPHERE, 30)

    py5.shape(s, 50, 50)
    emissive = s.get_emissive(0)
    py5.println(py5.red(emissive), py5.green(emissive), py5.blue(emissive))
```

</div></div>

</div>

## Description

Get the emissive color setting for one of a `Py5Shape` object's vertices. Use [](py5shape_set_emissive) to change the setting.

This method can only be used for a complete `Py5Shape` object, and never within a [](py5shape_begin_shape) and [](py5shape_end_shape) pair.

Underlying Processing method: PShape.getEmissive

## Signatures

```python
get_emissive(
    index: int,  # vertex index
    /,
) -> int
```

Updated on March 06, 2023 02:49:26am UTC
