Py5Vector.normalize()
=====================

Normalize the vector by setting the vector's magnitude to 1.0.

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

    v1 = py5.Py5Vector(3, 4)

    print("magnitude =", v1.mag)
    # magnitude = 5.0

    v1.normalize()

    print("magnitude =", v1.mag)
    # magnitude = 1.0

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Normalize the vector by setting the vector's magnitude to 1.0. This method cannot be used on a vector of zeros, because a vector of zeros cannot be normalized.

Signatures
----------

.. code:: python

    normalize() -> Py5Vector

Updated on September 01, 2022 14:08:27pm UTC

