Py5Graphics.specular()
======================

Sets the specular color of the materials used for shapes drawn to the Py5Graphics drawing surface, which sets the color of highlights.

Description
-----------

Sets the specular color of the materials used for shapes drawn to the Py5Graphics drawing surface, which sets the color of highlights. Specular refers to light which bounces off a surface in a preferred direction (rather than bouncing in all directions like a diffuse light). Use in combination with :doc:`py5graphics_emissive`, :doc:`py5graphics_ambient`, and :doc:`py5graphics_shininess` to set the material properties of shapes.

This method is the same as :doc:`sketch_specular` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_specular`.

Underlying Processing method: PGraphics.specular

Signatures
----------

.. code:: python

    specular(
        gray: float,  # value between black and white, by default 0 to 255
        /,
    ) -> None

    specular(
        rgb: int,  # color to set
        /,
    ) -> None

    specular(
        v1: float,  # red or hue value (depending on current color mode)
        v2: float,  # green or saturation value (depending on current color mode)
        v3: float,  # blue or brightness value (depending on current color mode)
        /,
    ) -> None
Updated on September 01, 2022 12:53:02pm UTC

