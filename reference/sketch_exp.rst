exp()
=====

Returns Euler's number e (2.71828...) raised to the power of the ``n`` parameter.

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
        v1 = py5.exp(1.0)
        py5.println(v1)  # Prints "2.718281828459045"

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Returns Euler's number e (2.71828...) raised to the power of the ``n`` parameter. This function is the compliment to :doc:`sketch_log`.

This function makes a call to the numpy ``exp()`` function.

Signatures
----------

.. code:: python

    exp(
        value: Union[float, npt.ArrayLike]  # exponent to raise
    ) -> Union[float, npt.NDArray]

Updated on September 01, 2022 14:08:27pm UTC

