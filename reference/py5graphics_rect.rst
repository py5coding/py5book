Py5Graphics.rect()
==================

Draws a rectangle to the Py5Graphics drawing surface.

Description
-----------

Draws a rectangle to the Py5Graphics drawing surface. A rectangle is a four-sided shape with every angle at ninety degrees. By default, the first two parameters set the location of the upper-left corner, the third sets the width, and the fourth sets the height. The way these parameters are interpreted, however, may be changed with the :doc:`py5graphics_rect_mode` function.

To draw a rounded rectangle, add a fifth parameter, which is used as the radius value for all four corners.

To use a different radius value for each corner, include eight parameters. When using eight parameters, the latter four set the radius of the arc at each corner separately, starting with the top-left corner and moving clockwise around the rectangle.

This method is the same as :doc:`sketch_rect` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_rect`.

Underlying Processing method: PGraphics.rect

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

