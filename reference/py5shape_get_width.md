# Py5Shape.get_width()

Get the `Py5Shape` object's width.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for get_width()](/images/reference/Py5Shape_get_width_0.png)

</div><div class="example-cell-code">

```python
def setup():
    s1 = py5.create_shape()
    s1.begin_shape()
    s1.vertex(20, 80)
    s1.vertex(80, 80)
    s1.vertex(50, 20)
    s1.end_shape(py5.CLOSE)
    py5.shape(s1)
    x_values = [s1.get_vertex_x(i) for i in range(s1.get_vertex_count())]
    py5.println(s1.get_width(), min(x_values), max(x_values))  # 80, 20, 80
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for get_width()](/images/reference/Py5Shape_get_width_1.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    py5.sphere_detail(8)
    s1 = py5.create_shape(py5.SPHERE, 40)
    x_values = [s1.get_vertex_x(i) for i in range(s1.get_vertex_count())]
    py5.shape(s1, 50, 50)
    py5.println(s1.get_width(), min(x_values), max(x_values))  # 80, -40, 40
```

</div></div>

</div>

## Description

Get the `Py5Shape` object's width. When using the `P2D` or `P3D` renderers, the returned value should be the width of the drawn shape. When using the default renderer, this will be the width of the drawing area, which will not necessarily be the same as the width of the drawn shape. Consider that the shape's vertices might have negative values or the shape may be offset from the shape's origin. To get the shape's actual width, calculate the range of the vertices obtained with [](py5shape_get_vertex_x).

Underlying Processing method: PShape.getWidth

## Signatures

```python
get_width() -> float
```

Updated on March 06, 2023 02:49:26am UTC
