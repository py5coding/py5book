Py5Graphics.no_smooth()
=======================

Draws all geometry and fonts with jagged (aliased) edges and images with hard edges between the pixels when enlarged rather than interpolating pixels.

Description
-----------

Draws all geometry and fonts with jagged (aliased) edges and images with hard edges between the pixels when enlarged rather than interpolating pixels.  Note that :doc:`py5graphics_smooth` is active by default, so it is necessary to call ``no_smooth()`` to disable smoothing of geometry, fonts, and images. The ``no_smooth()`` method can only be run once for a ``Py5Graphics`` object and it must be called before :doc:`py5graphics_begin_draw`.

This method is the same as :doc:`sketch_no_smooth` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_no_smooth`.

Underlying Processing method: PGraphics.noSmooth

Signatures
----------

.. code:: python

    no_smooth() -> None
Updated on September 01, 2022 12:53:02pm UTC

