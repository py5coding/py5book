# Py5Vector.dtype

Vector data type.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import numpy as np

v1 = py5.Py5Vector(1, 2, 3)
v2 = v1.astype(np.float16)

print(repr(v1.dtype))
# dtype('float64')
print(repr(v2.dtype))
# dtype('float16')
```

</div></div>

</div>

## Description

Vector data type. This will be one of `np.float16`, `np.float32`, `np.float64`, or `np.float128`.

Updated on March 06, 2023 02:49:26am UTC
