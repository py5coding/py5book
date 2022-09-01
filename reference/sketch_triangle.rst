triangle()
==========

A triangle is a plane created by connecting three points.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_triangle_0.png
    :alt: example picture for triangle()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        py5.triangle(30, 75, 58, 20, 86, 75)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

A triangle is a plane created by connecting three points. The first two arguments specify the first point, the middle two arguments specify the second point, and the last two arguments specify the third point.

Underlying Processing method: `triangle <https://processing.org/reference/triangle_.html>`_

Signatures
----------

.. code:: python

    triangle(
        x1: float,  # x-coordinate of the first point
        y1: float,  # y-coordinate of the first point
        x2: float,  # x-coordinate of the second point
        y2: float,  # y-coordinate of the second point
        x3: float,  # x-coordinate of the third point
        y3: float,  # y-coordinate of the third point
        /,
    ) -> None

Updated on September 01, 2022 16:36:02pm UTC

