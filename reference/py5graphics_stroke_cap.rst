Py5Graphics.stroke_cap()
========================

Sets the style for rendering line endings.

Description
-----------

Sets the style for rendering line endings. These ends are either squared, extended, or rounded, each of which specified with the corresponding parameters: ``SQUARE``, ``PROJECT``, and ``ROUND``. The default cap is ``ROUND``.

To make :doc:`py5graphics_point` appear square, use ``stroke_cap(PROJECT)``. Using ``stroke_cap(SQUARE)`` (no cap) causes points to become invisible.

This method is the same as :doc:`sketch_stroke_cap` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_stroke_cap`.

Underlying Processing method: PGraphics.strokeCap

Signatures
------

.. code:: python

    stroke_cap(
        cap: int,  # either SQUARE, PROJECT, or ROUND
        /,
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

