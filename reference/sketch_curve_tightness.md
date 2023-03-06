# curve_tightness()

Modifies the quality of forms created with [](sketch_curve) and [](sketch_curve_vertex).

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
# move the mouse left and right to see the curve change

def setup():
    py5.no_fill()


def draw():
    py5.background(204)
    t = py5.remap(py5.mouse_x, 0, py5.width, -5, 5)
    py5.curve_tightness(t)
    py5.begin_shape()
    py5.curve_vertex(10, 26)
    py5.curve_vertex(10, 26)
    py5.curve_vertex(83, 24)
    py5.curve_vertex(83, 61)
    py5.curve_vertex(25, 65)
    py5.curve_vertex(25, 65)
    py5.end_shape()
```

</div></div>

</div>

## Description

Modifies the quality of forms created with [](sketch_curve) and [](sketch_curve_vertex). The parameter `tightness` determines how the curve fits to the vertex points. The value 0.0 is the default value for `tightness` (this value defines the curves to be Catmull-Rom splines) and the value 1.0 connects all the points with straight lines. Values within the range -5.0 and 5.0 will deform the curves but will leave them recognizable and as values increase in magnitude, they will continue to deform.

Underlying Processing method: [curveTightness](https://processing.org/reference/curveTightness_.html)

## Signatures

```python
curve_tightness(
    tightness: float,  # amount of deformation from the original vertices
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
