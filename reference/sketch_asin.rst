asin()
======

The inverse of :doc:`sketch_sin`, returns the arc sine of a value.

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

    def setup():
        a = py5.PI/3
        s = py5.sin(a)
        a_s = py5.asin(s)
        # prints "1.04719757 : 0.86602541 : 1.04719757"
        py5.println(round(a, 8), ':', round(s, 8), ':', round(a_s, 8))

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        a = py5.PI + py5.PI/3
        s = py5.sin(a)
        a_s = py5.asin(s)
        # prints "4.18879027 : -0.86602543 : -1.04719761"
        py5.println(round(a, 8), ':', round(s, 8), ':', round(a_s, 8))

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

The inverse of :doc:`sketch_sin`, returns the arc sine of a value. This function expects the values in the range of -1 to 1 and values are returned in the range ``-HALF_PI`` to ``HALF_PI``.

This function makes a call to the numpy ``asin()`` function.

Signatures
----------

.. code:: python

    asin(
        value: Union[float, npt.ArrayLike]  # value in the range of -1 to 1 whose arc sine is to be returned
    ) -> Union[float, npt.NDArray]

Updated on September 01, 2022 14:08:27pm UTC

