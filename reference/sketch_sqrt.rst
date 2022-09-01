sqrt()
======

Calculates the square root of a number.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_sqrt_0.png
    :alt: example picture for sqrt()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.no_stroke()
        a = py5.sqrt(6561)  # Sets 'a' to 81
        b = py5.sqrt(625)   # Sets 'b' to 25
        c = py5.sqrt(1)     # Sets 'c' to 1
        py5.rect(0, 25, a, 10)
        py5.rect(0, 45, b, 10)
        py5.rect(0, 65, c, 10)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_sqrt_1.png
    :alt: example picture for sqrt()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.no_stroke()
        a = py5.sqrt(6561)  # Sets 'a' to 81
        b = py5.sqrt(-625)   # Sets 'b' to the complex number (0+25j)

        if isinstance(a, complex):
            py5.fill(255, 0, 0)
            py5.rect(0, 25, a.imag, 10)
        else:
            py5.fill(255)
            py5.rect(0, 25, a, 10)

        if isinstance(b, complex):
            py5.fill(255, 0, 0)
            py5.rect(0, 45, b.imag, 10)
        else:
            py5.fill(255)
            py5.rect(0, 45, b, 10)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Calculates the square root of a number. The square root of a positive number is always positive, even though there may be a valid negative root. The square root of a negative number is a complex number. In either case, the square root ``s`` of number ``a`` is such that ``s*s = a``. It is the opposite of squaring.

Python supports complex numbers, but such values cannot be passed to py5 drawing functions. When using the ``sqrt()`` function, you should check if the result is complex before using the value. You can also extract the real and imaginary components of the complex value with ``.real`` and ``.imag``. See the second example to learn how to do both of these things.

Signatures
----------

.. code:: python

    sqrt(
        value: Union[float, npt.NDArray]  # value to calculate the square root of
    ) -> Union[float, complex, npt.NDArray]

Updated on September 01, 2022 14:08:27pm UTC

