# Py5Vector.astype()

Create a new Py5Vector instance with a specified numpy dtype.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import numpy as np

v1 = py5.Py5Vector(1, 2, 3)
v2 = v1.astype(np.float16)

print(repr(v1))
# Py5Vector3D([1., 2., 3.])
print(repr(v2))
# Py5Vector3D([1., 2., 3.], dtype=float16)
```

</div></div>

</div>

## Description

Create a new Py5Vector instance with a specified numpy dtype. Only floating types (`np.float16`, `np.float32`, `np.float64`, and `np.float128`) are allowed.

## Signatures

```python
astype(
    dtype,  # numpy floating dtype
) -> Py5Vector
```

Updated on March 06, 2023 02:49:26am UTC
