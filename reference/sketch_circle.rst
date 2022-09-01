circle()
========

Draws a circle to the screen.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_circle_0.png
    :alt: example picture for circle()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.circle(56, 46, 55)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Draws a circle to the screen. By default, the first two parameters set the location of the center, and the third sets the shape's width and height. The origin may be changed with the :doc:`sketch_ellipse_mode` function.

Underlying Processing method: `circle <https://processing.org/reference/circle_.html>`_

Signatures
----------

.. code:: python

    circle(
        x: float,  # x-coordinate of the ellipse
        y: float,  # y-coordinate of the ellipse
        extent: float,  # width and height of the ellipse by default
        /,
    ) -> None
Updated on September 01, 2022 12:53:02pm UTC

