mag()
=====

Calculates the magnitude (or length) of a vector.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_mag_0.png
    :alt: example picture for mag()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        x1 = 20
        x2 = 80
        y1 = 30
        y2 = 70

        py5.line(0, 0, x1, y1)
        py5.println(py5.mag(x1, y1))  # Prints "36.05551"
        py5.line(0, 0, x2, y1)
        py5.println(py5.mag(x2, y1))  # Prints "85.44004"
        py5.line(0, 0, x1, y2)
        py5.println(py5.mag(x1, y2))  # Prints "72.8011"
        py5.line(0, 0, x2, y2)
        py5.println(py5.mag(x2, y2))  # Prints "106.30146"

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Calculates the magnitude (or length) of a vector. A vector is a direction in space commonly used in computer graphics and linear algebra. Because it has no "start" position, the magnitude of a vector can be thought of as the distance from the coordinate ``(0, 0)`` to its ``(x, y)`` value. Therefore, ``mag()`` is a shortcut for writing ``dist(0, 0, x, y)``.

Syntax
------

.. code:: python

    mag(a: float, b: float, /) -> float
    mag(a: float, b: float, c: float, /) -> float

Parameters
----------

* **a**: `float` - first value
* **b**: `float` - second value
* **c**: `float` - third value


Updated on November 08, 2021 12:26:18pm UTC

