Py5Graphics.rect_mode()
=======================

Modifies the location from which rectangles are drawn by changing the way in which parameters given to :doc:`py5graphics_rect` are intepreted.

Description
-----------

Modifies the location from which rectangles are drawn by changing the way in which parameters given to :doc:`py5graphics_rect` are intepreted.

The default mode is ``rect_mode(CORNER)``, which interprets the first two parameters of :doc:`py5graphics_rect` as the upper-left corner of the shape, while the third and fourth parameters are its width and height.

``rect_mode(CORNERS)`` interprets the first two parameters of :doc:`py5graphics_rect` as the location of one corner, and the third and fourth parameters as the location of the opposite corner.

``rect_mode(CENTER)`` interprets the first two parameters of :doc:`py5graphics_rect` as the shape's center point, while the third and fourth parameters are its width and height.

``rect_mode(RADIUS)`` also uses the first two parameters of :doc:`py5graphics_rect` as the shape's center point, but uses the third and fourth parameters to specify half of the shapes's width and height.

The parameter must be written in ALL CAPS because Python is a case-sensitive language.

This method is the same as :doc:`sketch_rect_mode` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_rect_mode`.

Underlying Processing method: PGraphics.rectMode

Signatures
------

.. code:: python

    rect_mode(
        mode: int,  # either CORNER, CORNERS, CENTER, or RADIUS
        /,
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

