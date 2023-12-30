# Py5Shape.set_emissive()

Sets a `Py5Shape` object's emissive color.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for set_emissive()](/images/reference/Py5Shape_set_emissive_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    py5.background(0)
    py5.directional_light(200, 200, 200, .5, 0, -1)
    py5.no_stroke()
    s = py5.create_shape(py5.SPHERE, 20)

    s.set_emissive("#003264")
    py5.shape(s, 50, 25)
    s.set_emissive("#643200")
    py5.shape(s, 50, 75)
```

</div></div>

</div>

## Description

Sets a `Py5Shape` object's emissive color. This is part of the material properties of a `Py5Shape` object.

The `emissive` parameter can be applied to the entire `Py5Shape` object or to a single vertex.

This method can only be used for a complete `Py5Shape` object, and never within a [](py5shape_begin_shape) and [](py5shape_end_shape) pair.

This method has additional color functionality that is not reflected in the method's signatures. For example, you can pass the name of a color (e.g. "green", "mediumpurple", etc). Look at the online ["All About Colors"](/integrations/colors) Python Ecosystem Integration tutorial for more information.

Underlying Processing method: PShape.setEmissive

## Signatures

```python
set_emissive(
    emissive: int,  # any color value
    /,
) -> None

set_emissive(
    index: int,  # vertex index
    emissive: int,  # any color value
    /,
) -> None
```

Updated on December 25, 2023 16:36:33pm UTC
