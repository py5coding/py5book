sq()
====

Squares a number (multiplies a number by itself).

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_sq_0.png
    :alt: example picture for sq()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.no_stroke()
        a = py5.sq(1)   # Sets 'a' to 1
        b = py5.sq(-5)  # Sets 'b' to 25
        c = py5.sq(9)   # Sets 'c' to 81
        py5.rect(0, 25, a, 10)
        py5.rect(0, 45, b, 10)
        py5.rect(0, 65, c, 10)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Squares a number (multiplies a number by itself). The result is always a positive number, as multiplying two negative numbers always yields a positive result. For example, ``-1 * -1 = 1``.

Signatures
----------

.. code:: python

    sq(
        value: Union[float, npt.NDArray]  # number to square
    ) -> Union[float, npt.NDArray]
Updated on September 01, 2022 12:53:02pm UTC

