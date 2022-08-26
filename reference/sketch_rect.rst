rect()
======

Draws a rectangle to the screen.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_rect_0.png
    :alt: example picture for rect()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.rect(30, 20, 55, 55)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_rect_1.png
    :alt: example picture for rect()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.rect(30, 20, 55, 55, 7)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_rect_2.png
    :alt: example picture for rect()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.rect(30, 20, 55, 55, 3, 6, 12, 18)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Draws a rectangle to the screen. A rectangle is a four-sided shape with every angle at ninety degrees. By default, the first two parameters set the location of the upper-left corner, the third sets the width, and the fourth sets the height. The way these parameters are interpreted, however, may be changed with the :doc:`sketch_rect_mode` function.

To draw a rounded rectangle, add a fifth parameter, which is used as the radius value for all four corners.

To use a different radius value for each corner, include eight parameters. When using eight parameters, the latter four set the radius of the arc at each corner separately, starting with the top-left corner and moving clockwise around the rectangle.

Underlying Processing method: `rect <https://processing.org/reference/rect_.html>`_

Signatures
------

.. code:: python

    rect(
        a: float,  # x-coordinate of the rectangle by default
        b: float,  # y-coordinate of the rectangle by default
        c: float,  # width of the rectangle by default
        d: float,  # height of the rectangle by default
        /,
    ) -> None

    rect(
        a: float,  # x-coordinate of the rectangle by default
        b: float,  # y-coordinate of the rectangle by default
        c: float,  # width of the rectangle by default
        d: float,  # height of the rectangle by default
        r: float,  # radii for all four corners
        /,
    ) -> None

    rect(
        a: float,  # x-coordinate of the rectangle by default
        b: float,  # y-coordinate of the rectangle by default
        c: float,  # width of the rectangle by default
        d: float,  # height of the rectangle by default
        tl: float,  # radius for top-left corner
        tr: float,  # radius for top-right corner
        br: float,  # radius for bottom-right corner
        bl: float,  # radius for bottom-left corner
        /,
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

