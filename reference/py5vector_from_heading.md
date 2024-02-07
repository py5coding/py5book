# Py5Vector.from_heading()

Class method to create a new vector with a given heading, measured in radians.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import numpy as np

v1 = py5.Py5Vector.from_heading(py5.radians(45))
print(v1)
# Py5Vector2D(0.70710678, 0.70710678)

v2 = py5.Py5Vector.from_heading(py5.radians(90), py5.radians(45), dtype=np.float16)
print(v2)
# Py5Vector3D(0.707, 0.707, 0.)

v3 = py5.Py5Vector.from_heading(py5.radians(90), py5.radians(45), py5.radians(45), dtype=np.float16)
print(v3)
# Py5Vector4D(0., 0.707, 0.5, 0.5)
```

</div></div>

</div>

## Description

Class method to create a new vector with a given heading, measured in radians. Use 1, 2, or 3 heading values for 2D, 3D, or 4D vectors, respectively.

For 2D vectors, the heading angle is the counter clockwise rotation of the vector relative to the positive x axis.

For 3D vectors, the heading values follow the ISO convention for spherical coordinates. The first heading value, inclination, is the angle relative to the positive z axis. The second heading value, azimuth, is the counter clockwise rotation of the vector around the z axis relative to the positive x axis. Note that this is slightly different from p5's `fromAngles()` function, which also follows the ISO convention but measures angles relative to the top of the screen (negative y axis).

For 4D vectors, the heading values follow the spherical coordinate system defined in Wikipedia's N-sphere article. The first heading value is the rotation around the zw plane relative to the positive x axis. The second heading value is the rotation around the xw plane relative to the positive y axis. The third heading value is the rotation around the xy plane relative to the positive z axis.

## Signatures

```python
from_heading(
    *heading,
    dtype: int = np.float64  # dtype of new vector to create
) -> Py5Vector
```

Updated on February 07, 2024 03:43:17am UTC
