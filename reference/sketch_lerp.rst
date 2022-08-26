lerp()
======

Calculates a number between two numbers at a specific increment.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_lerp_0.png
    :alt: example picture for lerp()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        a = 20
        b = 80
        c = py5.lerp(a, b, 0.2)
        d = py5.lerp(a, b, 0.5)
        e = py5.lerp(a, b, 0.8)
        py5.begin_shape(py5.POINTS)
        py5.vertex(a, 50)
        py5.vertex(b, 50)
        py5.vertex(c, 50)
        py5.vertex(d, 50)
        py5.vertex(e, 50)
        py5.end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_lerp_1.png
    :alt: example picture for lerp()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        x1 = 15
        y1 = 10
        x2 = 80
        y2 = 90
        py5.line(x1, y1, x2, y2)
        for i in range(10):
            x = py5.lerp(x1, x2, i/10) + 10
            y = py5.lerp(y1, y2, i/10)
            py5.point(x, y)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Calculates a number between two numbers at a specific increment. The ``amt`` parameter is the amount to interpolate between the two values where 0.0 equal to the first point, 0.1 is very near the first point, 0.5 is half-way in between, etc. The lerp function is convenient for creating motion along a straight path and for drawing dotted lines. If the ``amt`` parameter is greater than 1.0 or less than 0.0, the interpolated value will be outside of the range specified by the ``start`` and ``stop`` parameter values.

Signatures
------

.. code:: python

    lerp(
        start: Union[float, npt.NDArray],  # first value
        stop: Union[float, npt.NDArray],  # second value
        amt: Union[float, npt.NDArray],  # float between 0.0 and 1.0
    ) -> Union[float, npt.NDArray]
Updated on August 25, 2022 20:01:47pm UTC

