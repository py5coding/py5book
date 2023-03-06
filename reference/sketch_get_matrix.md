# get_matrix()

Get the current matrix as a numpy array.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for get_matrix()](/images/reference/Sketch_get_matrix_0.png)

</div><div class="example-cell-code">

```python
def setup():
    global matrix
    py5.size(100, 100, py5.P3D)
    py5.no_fill()
    py5.translate(50, 50, 0)
    py5.rotate_y(py5.PI/6)
    matrix = py5.get_matrix()
    py5.println(matrix)
    py5.println(matrix.dtype)
    py5.stroke(153)
    py5.box(50)
```

</div></div>

</div>

## Description

Get the current matrix as a numpy array. Use the `target` parameter to put the matrix data in a properly sized and typed numpy array.

Underlying Processing method: getMatrix

## Signatures

```python
get_matrix() -> npt.NDArray[np.floating]

get_matrix(
    target: npt.NDArray[np.floating],  # transformation matrix with a shape of 2x3 for 2D transforms or 4x4 for 3D transforms
    /,
) -> npt.NDArray[np.floating]
```

Updated on March 06, 2023 02:49:26am UTC
