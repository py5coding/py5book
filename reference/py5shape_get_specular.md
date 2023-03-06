# Py5Shape.get_specular()

Get the specular color setting for one of a `Py5Shape` object's vertices.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for get_specular()](/images/reference/Py5Shape_get_specular_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    py5.background(0)
    py5.light_specular(255, 255, 255)
    py5.directional_light(204, 204, 204, 0, 0, -1)
    py5.no_stroke()
    s = py5.create_shape(py5.SPHERE, 30)

    py5.shape(s, 50, 50)
    specular = s.get_specular(0)
    py5.println(py5.red(specular), py5.green(specular), py5.blue(specular))
```

</div></div>

</div>

## Description

Get the specular color setting for one of a `Py5Shape` object's vertices. Use [](py5shape_set_specular) to change the setting.

This method can only be used for a complete `Py5Shape` object, and never within a [](py5shape_begin_shape) and [](py5shape_end_shape) pair.

Underlying Processing method: PShape.getSpecular

## Signatures

```python
get_specular(
    index: int,  # vertex index
    /,
) -> int
```

Updated on March 06, 2023 02:49:26am UTC
