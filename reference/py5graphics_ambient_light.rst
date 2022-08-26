Py5Graphics.ambient_light()
===========================

Adds an ambient light.

Description
-----------

Adds an ambient light. Ambient light doesn't come from a specific direction, the rays of light have bounced around so much that objects are evenly lit from all sides. Ambient lights are almost always used in combination with other types of lights. The ``v1``, ``v2``, and ``v3`` parameters are interpreted as either ``RGB`` or ``HSB`` values, depending on the current color mode.

This method is the same as :doc:`sketch_ambient_light` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_ambient_light`.

Underlying Processing method: PGraphics.ambientLight

Signatures
------

.. code:: python

    ambient_light(
        v1: float,  # red or hue value (depending on current color mode)
        v2: float,  # green or saturation value (depending on current color mode)
        v3: float,  # blue or brightness value (depending on current color mode)
        /,
    ) -> None

    ambient_light(
        v1: float,  # red or hue value (depending on current color mode)
        v2: float,  # green or saturation value (depending on current color mode)
        v3: float,  # blue or brightness value (depending on current color mode)
        x: float,  # x-coordinate of the light
        y: float,  # y-coordinate of the light
        z: float,  # z-coordinate of the light
        /,
    ) -> None
Updated on August 25, 2022 19:59:03pm UTC

