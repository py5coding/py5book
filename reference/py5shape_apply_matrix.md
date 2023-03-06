# Py5Shape.apply_matrix()

Apply a transformation matrix to a `Py5Shape` object.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    global s
    s = py5.create_shape(py5.RECT, -40, -40, 80, 80)


def draw():
    py5.background(255)
    if py5.is_mouse_pressed:
        s.apply_matrix(0.99, 0, 0, 0, 0.99, 0)
    else:
        s.reset_matrix()
    py5.shape(s, py5.width / 2, py5.height / 2)
```

</div></div>

</div>

## Description

Apply a transformation matrix to a `Py5Shape` object. This can be used to scale, rotate, and translate a shape with one call.

Making productive use of this method requires some knowledge of 2D or 3D transformation matrices, and perhaps some knowledge of Processing's source code.

Transformations are cummulative and therefore will be applied on top of existing transformations. Use [](py5shape_reset_matrix) to set the transformation matrix to the identity matrix.

Underlying Processing method: PShape.applyMatrix

## Signatures

```python
apply_matrix(
    n00: float,  # numeric value in row 0 and column 0 of the matrix
    n01: float,  # numeric value in row 0 and column 1 of the matrix
    n02: float,  # numeric value in row 0 and column 2 of the matrix
    n03: float,  # numeric value in row 0 and column 3 of the matrix
    n10: float,  # numeric value in row 1 and column 0 of the matrix
    n11: float,  # numeric value in row 1 and column 1 of the matrix
    n12: float,  # numeric value in row 1 and column 2 of the matrix
    n13: float,  # numeric value in row 1 and column 3 of the matrix
    n20: float,  # numeric value in row 2 and column 0 of the matrix
    n21: float,  # numeric value in row 2 and column 1 of the matrix
    n22: float,  # numeric value in row 2 and column 2 of the matrix
    n23: float,  # numeric value in row 2 and column 3 of the matrix
    n30: float,  # numeric value in row 3 and column 0 of the matrix
    n31: float,  # numeric value in row 3 and column 1 of the matrix
    n32: float,  # numeric value in row 3 and column 2 of the matrix
    n33: float,  # numeric value in row 3 and column 3 of the matrix
    /,
) -> None

apply_matrix(
    n00: float,  # numeric value in row 0 and column 0 of the matrix
    n01: float,  # numeric value in row 0 and column 1 of the matrix
    n02: float,  # numeric value in row 0 and column 2 of the matrix
    n10: float,  # numeric value in row 1 and column 0 of the matrix
    n11: float,  # numeric value in row 1 and column 1 of the matrix
    n12: float,  # numeric value in row 1 and column 2 of the matrix
    /,
) -> None

apply_matrix(
    source: npt.NDArray[np.floating],  # transformation matrix with a shape of 2x3 for 2D transforms or 4x4 for 3D transforms
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
