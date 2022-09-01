bezier()
========

Draws a Bezier curve on the screen.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_bezier_0.png
    :alt: example picture for bezier()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.no_fill()
        py5.stroke(255, 102, 0)
        py5.line(85, 20, 10, 10)
        py5.line(90, 90, 15, 80)
        py5.stroke(0, 0, 0)
        py5.bezier(85, 20, 10, 10, 90, 90, 15, 80)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_bezier_1.png
    :alt: example picture for bezier()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.no_fill()
        py5.stroke(255, 102, 0)
        py5.line(30, 20, 80, 5)
        py5.line(80, 75, 30, 75)
        py5.stroke(0, 0, 0)
        py5.bezier(30, 20, 80, 5, 80, 75, 30, 75)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Draws a Bezier curve on the screen. These curves are defined by a series of anchor and control points. The first two parameters specify the first anchor point and the last two parameters specify the other anchor point. The middle parameters specify the control points which define the shape of the curve. Bezier curves were developed by French engineer Pierre Bezier. Using the 3D version requires rendering with ``P3D``.

Underlying Processing method: `bezier <https://processing.org/reference/bezier_.html>`_

Signatures
----------

.. code:: python

    bezier(
        x1: float,  # coordinates for the first anchor point
        y1: float,  # coordinates for the first anchor point
        x2: float,  # coordinates for the first control point
        y2: float,  # coordinates for the first control point
        x3: float,  # coordinates for the second control point
        y3: float,  # coordinates for the second control point
        x4: float,  # coordinates for the second anchor point
        y4: float,  # coordinates for the second anchor point
        /,
    ) -> None

    bezier(
        x1: float,  # coordinates for the first anchor point
        y1: float,  # coordinates for the first anchor point
        z1: float,  # coordinates for the first anchor point
        x2: float,  # coordinates for the first control point
        y2: float,  # coordinates for the first control point
        z2: float,  # coordinates for the first control point
        x3: float,  # coordinates for the second control point
        y3: float,  # coordinates for the second control point
        z3: float,  # coordinates for the second control point
        x4: float,  # coordinates for the second anchor point
        y4: float,  # coordinates for the second anchor point
        z4: float,  # coordinates for the second anchor point
        /,
    ) -> None

Updated on September 01, 2022 14:08:27pm UTC

