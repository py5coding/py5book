Py5Graphics.ambient()
=====================

Sets the ambient reflectance for shapes drawn to the screen.

Description
-----------

Sets the ambient reflectance for shapes drawn to the screen. This is combined with the ambient light component of the environment. The color components set through the parameters define the reflectance. For example in the default color mode, setting ``ambient(255, 127, 0)``, would cause all the red light to reflect and half of the green light to reflect. Use in combination with :doc:`py5graphics_emissive`, :doc:`py5graphics_specular`, and :doc:`py5graphics_shininess` to set the material properties of shapes.

This method is the same as :doc:`sketch_ambient` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_ambient`.

Underlying Processing method: PGraphics.ambient

Signatures
------

.. code:: python

    ambient(
        gray: float,  # number specifying value between white and black
        /,
    ) -> None

    ambient(
        rgb: int,  # any value of the color datatype
        /,
    ) -> None

    ambient(
        v1: float,  # red or hue value (depending on current color mode)
        v2: float,  # green or saturation value (depending on current color mode)
        v3: float,  # blue or brightness value (depending on current color mode)
        /,
    ) -> None
Updated on August 25, 2022 19:59:03pm UTC

