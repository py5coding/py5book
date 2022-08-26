Py5Vector.heading
=================

The vector's heading, measured in radians.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    import numpy as np

    v1 = py5.Py5Vector(20, 20)
    v1.heading = py5.radians(135)
    print(v1)
    # Py5Vector2D(-20., 20.)
    print(v1.heading)
    # 2.356194490192345

    v2 = py5.Py5Vector(10, 10, 10, dtype=np.float16)
    v2.heading = py5.radians(45), py5.radians(135)
    print(v2)
    # Py5Vector3D(-8.664, 8.664, 12.25)
    print(v2.heading)
    # (0.7855022650013651, 2.35546875)

    v3 = py5.Py5Vector(5, 5, 5, 5, dtype=np.float16)
    v3.heading = py5.radians(45), py5.radians(45), py5.radians(90)
    print(v3)
    # Py5Vector4D(7.07, 5., 0., 5.)
    print(v3.heading)
    # (0.7854515748642288, 0.7853981633974483, 1.5707963267948966)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

The vector's heading, measured in radians. The heading will be measured with 1, 2, or 3 numbers for 2D, 3D, or 4D vectors, respectively.

For 2D vectors, the heading angle is the counter clockwise rotation of the vector relative to the positive x axis.

For 3D vectors, the heading values follow the ISO convention for spherical coordinates. The first heading value, inclination, is the angle relative to the positive z axis. The second heading value, azimuth, is the counter clockwise rotation of the vector around the z axis relative to the positive x axis. Note that this is slightly different from p5's ``fromAngles()`` function, which also follows the ISO convention but measures angles relative to the top of the screen (negative y axis).

For 4D vectors, the heading values follow the spherical coordinate system defined in Wikipedia's N-sphere article. The first heading value is the rotation around the zw plane relative to the positive x axis. The second heading value is the rotation around the xw plane relative to the positive y axis. The third heading value is the rotation around the xy plane relative to the positive z axis.

Updated on August 25, 2022 20:01:47pm UTC

