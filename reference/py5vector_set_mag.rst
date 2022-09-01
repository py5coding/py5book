Py5Vector.set_mag()
===================

Set the vector's magnitude.

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

    v1.set_mag(1)

    print("magnitude =", v1.mag)
    # magnitude = 1.0

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Set the vector's magnitude. Setting this to a non-negative number will adjust the vector's magnitude to that value. Negative values will result in an error.

Signatures
----------

.. code:: python

    set_mag(
        mag: float,  # vector magnitude
    ) -> Py5Vector

Updated on September 01, 2022 14:08:27pm UTC

