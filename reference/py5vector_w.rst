Py5Vector.w
===========

The vector's w dimension value.

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

    v = py5.Py5Vector(1, 2, 3, 4)

    print(v.x, v.y, v.z, v.w)
    # 1.0, 2.0, 3.0, 4.0

    v.x = 0
    v.y += 10
    v.z += 100
    v.w += 1000

    print(v.x, v.y, v.z, v.w)
    # 0.0, 12.0, 103.0, 1004.0

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

The vector's w dimension value. This is the vector's 4th dimension, and is only applicable to 4D vectors.


Updated on January 16, 2022 16:51:21pm UTC

