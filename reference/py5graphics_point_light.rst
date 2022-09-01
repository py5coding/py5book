Py5Graphics.point_light()
=========================

Adds a point light.

Description
-----------

Adds a point light. The ``v1``, ``v2``, and ``v3`` parameters are interpreted as either RGB or HSB values, depending on the current color mode. The ``x``, ``y``, and ``z`` parameters set the position of the light.

This method is the same as :doc:`sketch_point_light` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_point_light`.

Underlying Processing method: PGraphics.pointLight

Signatures
----------

.. code:: python

    point_light(
        v1: float,  # red or hue value (depending on current color mode)
        v2: float,  # green or saturation value (depending on current color mode)
        v3: float,  # blue or brightness value (depending on current color mode)
        x: float,  # x-coordinate of the light
        y: float,  # y-coordinate of the light
        z: float,  # z-coordinate of the light
        /,
    ) -> None
Updated on September 01, 2022 12:53:02pm UTC

