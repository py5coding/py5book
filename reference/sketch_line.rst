line()
======

Draws a line (a direct path between two points) to the screen.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_line_0.png
    :alt: example picture for line()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.line(30, 20, 85, 75)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_line_1.png
    :alt: example picture for line()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.line(30, 20, 85, 20)
        py5.stroke(126)
        py5.line(85, 20, 85, 75)
        py5.stroke(255)
        py5.line(85, 75, 30, 75)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_line_2.png
    :alt: example picture for line()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        # drawing lines in 3D requires P3D
        # as a parameter to size()
        py5.line(30, 20, 0, 85, 20, 15)
        py5.stroke(126)
        py5.line(85, 20, 15, 85, 75, 0)
        py5.stroke(255)
        py5.line(85, 75, 0, 30, 75, -50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Draws a line (a direct path between two points) to the screen. The version of ``line()`` with four parameters draws the line in 2D.  To color a line, use the :doc:`sketch_stroke` function. A line cannot be filled, therefore the :doc:`sketch_fill` function will not affect the color of a line. 2D lines are drawn with a width of one pixel by default, but this can be changed with the :doc:`sketch_stroke_weight` function. The version with six parameters allows the line to be placed anywhere within XYZ space. Drawing this shape in 3D with the ``z`` parameter requires the ``P3D`` parameter in combination with :doc:`sketch_size` as shown in the third example.

Underlying Processing method: `line <https://processing.org/reference/line_.html>`_

Signatures
------

.. code:: python

    line(
        x1: float,  # x-coordinate of the first point
        y1: float,  # y-coordinate of the first point
        x2: float,  # x-coordinate of the second point
        y2: float,  # y-coordinate of the second point
        /,
    ) -> None

    line(
        x1: float,  # x-coordinate of the first point
        y1: float,  # y-coordinate of the first point
        z1: float,  # z-coordinate of the first point
        x2: float,  # x-coordinate of the second point
        y2: float,  # y-coordinate of the second point
        z2: float,  # z-coordinate of the second point
        /,
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

