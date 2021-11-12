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
    :number-lines:

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

Syntax
------

.. code:: python

    triangle(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, /) -> None

Parameters
----------

* **x1**: `float` - x-coordinate of the first point
* **x2**: `float` - x-coordinate of the second point
* **x3**: `float` - x-coordinate of the third point
* **y1**: `float` - y-coordinate of the first point
* **y2**: `float` - y-coordinate of the second point
* **y3**: `float` - y-coordinate of the third point


Updated on November 12, 2021 11:30:58am UTC

