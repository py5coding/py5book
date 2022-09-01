Py5Vector.set_mag_sq()
======================

Set the vector's squared magnitude.

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
    print("magnitude squared =", v1.mag_sq)
    # magnitude squared = 25.0

    v1.set_mag_sq(100)

    print("magnitude =", v1.mag)
    # magnitude = 10.0
    print("magnitude squared =", v1.mag_sq)
    # magnitude squared = 100.0

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Set the vector's squared magnitude. Setting this to a non-negative number will adjust the vector's squared magnitude to that value. Negative values will result in an error.

Signatures
----------

.. code:: python

    set_mag_sq(
        mag_sq: float,  # vector magnitude squared
    ) -> Py5Vector
Updated on September 01, 2022 12:53:02pm UTC

