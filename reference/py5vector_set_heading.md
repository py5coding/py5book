# Py5Vector.set_heading()

Align vector with the specified heading.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import numpy as np

v1 = py5.Py5Vector(20, 20)
v1.set_heading(py5.radians(135))
print(v1)
# Py5Vector2D(-20., 20.)
print(v1.heading)
# 2.356194490192345

v2 = py5.Py5Vector(10, 10, 10, dtype=np.float16)
v2.set_heading(py5.radians(45), py5.radians(135))
print(v2)
# Py5Vector3D(-8.664, 8.664, 12.25)
print(v2.heading)
# (0.7855022650013651, 2.35546875)

v3 = py5.Py5Vector(5, 5, 5, 5, dtype=np.float16)
v3.set_heading(py5.radians(45), py5.radians(45), py5.radians(90))
print(v3)
# Py5Vector4D(7.07, 5., 0., 5.)
print(v3.heading)
# (0.7854515748642288, 0.7853981633974483, 1.5707963267948966)
```

</div></div>

</div>

## Description

Align vector with the specified heading. Use 1, 2, or 3 heading values for 2D, 3D, or 4D vectors, respectively. The number of heading values passed to this method must match the vector's actual dimension.

For 2D vectors, the heading angle is the counter clockwise rotation of the vector relative to the positive x axis.

For 3D vectors, the heading values follow the ISO convention for spherical coordinates. The first heading value, inclination, is the angle relative to the positive z axis. The second heading value, azimuth, is the counter clockwise rotation of the vector around the z axis relative to the positive x axis. Note that this is slightly different from p5's `fromAngles()` function, which also follows the ISO convention but measures angles relative to the top of the screen (negative y axis).

For 4D vectors, the heading values follow the spherical coordinate system defined in Wikipedia's N-sphere article. The first heading value is the rotation around the zw plane relative to the positive x axis. The second heading value is the rotation around the xw plane relative to the positive y axis. The third heading value is the rotation around the xy plane relative to the positive z axis.

## Signatures

```python
set_heading(
    *heading,
) -> (
    Py5Vector
)
```

Updated on April 13, 2025 05:05:46am UTC
