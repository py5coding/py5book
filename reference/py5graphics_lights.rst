Py5Graphics.lights()
====================

Sets the default ambient light, directional light, falloff, and specular values.

Description
-----------

Sets the default ambient light, directional light, falloff, and specular values. The defaults are ``ambientLight(128, 128, 128)`` and ``directionalLight(128, 128, 128, 0, 0, -1)``, ``lightFalloff(1, 0, 0)``, and ``lightSpecular(0, 0, 0)``.

This method is the same as :doc:`sketch_lights` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_lights`.

Underlying Processing method: PGraphics.lights

Syntax
------

.. code:: python

    lights() -> None

Updated on November 12, 2021 11:30:58am UTC

