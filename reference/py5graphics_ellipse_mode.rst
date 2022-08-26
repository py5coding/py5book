Py5Graphics.ellipse_mode()
==========================

Modifies the location from which ellipses are drawn by changing the way in which parameters given to :doc:`py5graphics_ellipse` are intepreted.

Description
-----------

Modifies the location from which ellipses are drawn by changing the way in which parameters given to :doc:`py5graphics_ellipse` are intepreted.

The default mode is ``ellipse_mode(CENTER)``, which interprets the first two parameters of :doc:`py5graphics_ellipse` as the shape's center point, while the third and fourth parameters are its width and height.

``ellipse_mode(RADIUS)`` also uses the first two parameters of :doc:`py5graphics_ellipse` as the shape's center point, but uses the third and fourth parameters to specify half of the shapes's width and height.

``ellipse_mode(CORNER)`` interprets the first two parameters of :doc:`py5graphics_ellipse` as the upper-left corner of the shape, while the third and fourth parameters are its width and height.

``ellipse_mode(CORNERS)`` interprets the first two parameters of :doc:`py5graphics_ellipse` as the location of one corner of the ellipse's bounding box, and the third and fourth parameters as the location of the opposite corner.

The parameter must be written in ALL CAPS because Python is a case-sensitive language.

This method is the same as :doc:`sketch_ellipse_mode` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_ellipse_mode`.

Underlying Processing method: PGraphics.ellipseMode

Signatures
------

.. code:: python

    ellipse_mode(
        mode: int,  # either CENTER, RADIUS, CORNER, or CORNERS
        /,
    ) -> None
Updated on August 25, 2022 19:59:03pm UTC

