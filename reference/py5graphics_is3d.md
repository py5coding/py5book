# Py5Graphics.is3d()

Boolean value reflecting if the Py5Graphics object is or is not a 3D renderer.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.size(200, 200)
    g = py5.get_graphics()

    # prints False
    print(g.is3d())
```

</div></div>

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.size(200, 200, py5.P3D)
    g = py5.get_graphics()

    # prints True
    print(g.is3d())
```

</div></div>

</div>

## Description

Boolean value reflecting if the Py5Graphics object is or is not a 3D renderer.

This will be `True` if the renderer is a 3D renderer such as `P3D`.

Underlying Processing method: PGraphics.is3D

## Signatures

```python
is3d() -> bool
```

Updated on November 05, 2024 03:06:24am UTC
