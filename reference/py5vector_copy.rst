Py5Vector.copy
==============

Create an identical copy of this Py5Vector instance.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    v1 = py5.Py5Vector(1, 2, 3)

    print(v1)
    # Py5Vector3D([1., 2., 3.])

    v2 = 10 * v1.copy

    print(v1)
    # Py5Vector3D([1., 2., 3.])
    print(v2)
    # Py5Vector3D([10., 20., 30.])

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Create an identical copy of this Py5Vector instance.

Updated on September 01, 2022 16:36:02pm UTC

