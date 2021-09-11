curve()
=======

Draws a curved line on the screen.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_curve_0.png
    :alt: example picture for curve()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.no_fill()
        py5.stroke(255, 102, 0)
        py5.curve(5, 26, 5, 26, 73, 24, 73, 61)
        py5.stroke(0)
        py5.curve(5, 26, 73, 24, 73, 61, 15, 65)
        py5.stroke(255, 102, 0)
        py5.curve(73, 24, 73, 61, 15, 65, 15, 65)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Draws a curved line on the screen. The first and second parameters specify the beginning control point and the last two parameters specify the ending control point. The middle parameters specify the start and stop of the curve. Longer curves can be created by putting a series of ``curve()`` functions together or using :doc:`sketch_curve_vertex`. An additional function called :doc:`sketch_curve_tightness` provides control for the visual quality of the curve. The ``curve()`` function is an implementation of Catmull-Rom splines. Using the 3D version requires rendering with ``P3D``.

Underlying Java method: `curve <https://processing.org/reference/curve_.html>`_

Syntax
------

.. code:: python

    curve(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, /) -> None
    curve(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, x3: float, y3: float, z3: float, x4: float, y4: float, z4: float, /) -> None

Parameters
----------

* **x1**: `float` - coordinates for the beginning control point
* **x2**: `float` - coordinates for the first point
* **x3**: `float` - coordinates for the second point
* **x4**: `float` - coordinates for the ending control point
* **y1**: `float` - coordinates for the beginning control point
* **y2**: `float` - coordinates for the first point
* **y3**: `float` - coordinates for the second point
* **y4**: `float` - coordinates for the ending control point
* **z1**: `float` - coordinates for the beginning control point
* **z2**: `float` - coordinates for the first point
* **z3**: `float` - coordinates for the second point
* **z4**: `float` - coordinates for the ending control point


Updated on September 11, 2021 16:51:34pm UTC

