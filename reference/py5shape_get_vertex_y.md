# Py5Shape.get_vertex_y()

Get the value of the y coordinate for the vertex `index`.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for get_vertex_y()](/images/reference/Py5Shape_get_vertex_y_0.png)

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
    y_values = [s1.get_vertex_y(i) for i in range(s1.get_vertex_count())]
    py5.println(s1.get_height(), min(y_values), max(y_values))  # 80, 20, 80
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for get_vertex_y()](/images/reference/Py5Shape_get_vertex_y_1.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    py5.sphere_detail(8)
    s1 = py5.create_shape(py5.SPHERE, 40)
    y_values = [s1.get_vertex_y(i) for i in range(s1.get_vertex_count())]
    py5.shape(s1, 50, 50)
    py5.println(s1.get_height(), min(y_values), max(y_values))  # 80, -40, 40
```

</div></div>

</div>

## Description

Get the value of the y coordinate for the vertex `index`.

Underlying Processing method: PShape.getVertexY

## Signatures

```python
get_vertex_y(
    index: int,  # vertex index
    /,
) -> float
```

Updated on March 06, 2023 02:49:26am UTC
