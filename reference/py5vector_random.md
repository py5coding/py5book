# Py5Vector.random()

Create a new vector with random values.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
v_2d = py5.Py5Vector2D.random()
print(v_2d)
# Py5Vector2D(-0.95511074, 0.29624901)
v_3d = py5.Py5Vector3D.random()
print(v_3d)
# Py5Vector3D(0.448865, -0.84838302, 0.28065363)
v_4d = py5.Py5Vector4D.random()
print(v_4d)
# Py5Vector4D(0.46938054, 0.14506664, 0.61450653, 0.61726761)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for random()](/images/reference/Py5Vector_random_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.background(128)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.stroke(0)
    for _ in range(25):
        v = 40 * py5.Py5Vector.random(dim=2)
        py5.line(0, 0, v.x, v.y)
```

</div></div>

</div>

## Description

Create a new vector with random values. Use the `dim` parameter to specify if the vector should have 2, 3, or 4 dimensions.

The new vector will have a magnitude of 1 and a heading that is uniformly distributed across all possible headings for a vector with the given dimension.

When used as a `Py5Vector` class method, the `dim` parameter is required to specify what the new vector's dimension should be. When used as a class method for the `Py5Vector2D`, `Py5Vector3D`, or `Py5Vector4D` child classes, the `dim` parameter is optional and will default to the dimension implied by the specific class. When used as a method on a vector instance, the `dim` parameter is also optional and will default to the vector instance's dimension. See the example code for examples of all of these use cases.

## Signatures

```python
random(
    dim: int,  # dimension of the random vector to create
    *,
    dtype: type = np.float64  # dtype of the random vector to create
) -> Py5Vector
```

Updated on February 07, 2024 03:43:17am UTC
