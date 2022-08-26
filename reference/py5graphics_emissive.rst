Py5Graphics.emissive()
======================

Sets the emissive color of the material used for drawing shapes drawn to the screen.

Description
-----------

Sets the emissive color of the material used for drawing shapes drawn to the screen. Use in combination with :doc:`py5graphics_ambient`, :doc:`py5graphics_specular`, and :doc:`py5graphics_shininess` to set the material properties of shapes.

This method is the same as :doc:`sketch_emissive` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_emissive`.

Underlying Processing method: PGraphics.emissive

Signatures
------

.. code:: python

    emissive(
        gray: float,  # value between black and white, by default 0 to 255
        /,
    ) -> None

    emissive(
        rgb: int,  # color to set
        /,
    ) -> None

    emissive(
        v1: float,  # red or hue value (depending on current color mode)
        v2: float,  # green or saturation value (depending on current color mode)
        v3: float,  # blue or brightness value (depending on current color mode)
        /,
    ) -> None
Updated on August 25, 2022 19:59:03pm UTC

