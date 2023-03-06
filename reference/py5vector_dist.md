# Py5Vector.dist()

Calculate the distance between two vectors.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for dist()](/images/reference/Py5Vector_dist_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.background(128)
    v1 = py5.Py5Vector(22.8, 31.4)
    v2 = py5.Py5Vector(87.2, 72.4)
    py5.line(v1.x, v1.y, v2.x, v2.y)
    py5.text(f'dist = {v1.dist(v2):.2f}', 5, 15)
```

</div></div>

</div>

## Description

Calculate the distance between two vectors.

## Signatures

```python
dist(
    other: Union[Py5Vector, np.ndarray]  # vector to calculate the distance from
) -> Union[float, np.ndarray[np.floating]]
```

Updated on March 06, 2023 02:49:26am UTC
