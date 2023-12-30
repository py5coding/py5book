# Py5Shape.set_specular()

Sets the specular color of a `Py5Shape` object's material, which sets the color of highlight.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for set_specular()](/images/reference/Py5Shape_set_specular_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    py5.background(0)
    py5.light_specular(255, 255, 255)
    py5.directional_light(204, 204, 204, 0, 0, -1)
    py5.no_stroke()
    s = py5.create_shape(py5.SPHERE, 20)

    s.set_specular("#FFFFFF")
    py5.shape(s, 50, 25)
    s.set_specular("#CC6600")
    py5.shape(s, 50, 75)
```

</div></div>

</div>

## Description

Sets the specular color of a `Py5Shape` object's material, which sets the color of highlight. This is part of the material properties of a `Py5Shape` object.

The `specular` parameter can be applied to the entire `Py5Shape` object or to a single vertex.

This method can only be used for a complete `Py5Shape` object, and never within a [](py5shape_begin_shape) and [](py5shape_end_shape) pair.

This method has additional color functionality that is not reflected in the method's signatures. For example, you can pass the name of a color (e.g. "green", "mediumpurple", etc). Look at the online ["All About Colors"](/integrations/colors) Python Ecosystem Integration tutorial for more information.

Underlying Processing method: PShape.setSpecular

## Signatures

```python
set_specular(
    index: int,  # vertex index
    specular: int,  # any color value
    /,
) -> None

set_specular(
    specular: int,  # any color value
    /,
) -> None
```

Updated on December 25, 2023 16:36:33pm UTC
