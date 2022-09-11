Py5Graphics.box()
=================

A box is an extruded rectangle.

Description
-----------

A box is an extruded rectangle. A box with equal dimensions on all sides is a cube.

This method is the same as :doc:`sketch_box` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_box`.

Underlying Processing method: PGraphics.box

Signatures
----------

.. code:: python

    box(
        size: float,  # dimension of the box in all dimensions (creates a cube)
        /,
    ) -> None

    box(
        w: float,  # dimension of the box in the x-dimension
        h: float,  # dimension of the box in the y-dimension
        d: float,  # dimension of the box in the z-dimension
        /,
    ) -> None

Updated on September 01, 2022 14:08:27pm UTC

