Py5Vector.tolist()
==================

Return the vector's values as a list.

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

    v1 = py5.Py5Vector(1, 2, 3)

    print(v1.tolist())
    # [1.0, 2.0, 3.0]

    print(type(v1.tolist()))
    # <class 'list'>

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Return the vector's values as a list. The length of the list will be equal to the vector's dimension.

Signatures
----------

.. code:: python

    tolist() -> list[float]

Updated on September 01, 2022 14:08:27pm UTC

