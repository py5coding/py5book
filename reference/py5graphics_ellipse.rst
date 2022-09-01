Py5Graphics.ellipse()
=====================

Draws an ellipse (oval) to the screen.

Description
-----------

Draws an ellipse (oval) to the screen. An ellipse with equal width and height is a circle. By default, the first two parameters set the location, and the third and fourth parameters set the shape's width and height. The origin may be changed with the :doc:`py5graphics_ellipse_mode` function.

This method is the same as :doc:`sketch_ellipse` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_ellipse`.

Underlying Processing method: PGraphics.ellipse

Signatures
----------

.. code:: python

    ellipse(
        a: float,  # x-coordinate of the ellipse
        b: float,  # y-coordinate of the ellipse
        c: float,  # width of the ellipse by default
        d: float,  # height of the ellipse by default
        /,
    ) -> None

Updated on September 01, 2022 14:08:27pm UTC

