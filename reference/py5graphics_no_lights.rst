Py5Graphics.no_lights()
=======================

Disable all lighting.

Description
-----------

Disable all lighting. Lighting is turned off by default and enabled with the :doc:`py5graphics_lights` function. This function can be used to disable lighting so that 2D geometry (which does not require lighting) can be drawn after a set of lighted 3D geometry.

This method is the same as :doc:`sketch_no_lights` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_no_lights`.

Underlying Processing method: PGraphics.noLights

Signatures
------

.. code:: python

    no_lights() -> None
Updated on August 25, 2022 20:01:47pm UTC

