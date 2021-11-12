Py5Graphics.texture_wrap()
==========================

Defines if textures repeat or draw once within a texture map.

Description
-----------

Defines if textures repeat or draw once within a texture map. The two parameters are ``CLAMP`` (the default behavior) and ``REPEAT``. This function only works with the ``P2D`` and ``P3D`` renderers.

This method is the same as :doc:`sketch_texture_wrap` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_texture_wrap`.

Underlying Processing method: PGraphics.textureWrap

Syntax
------

.. code:: python

    texture_wrap(wrap: int, /) -> None

Parameters
----------

* **wrap**: `int` - Either CLAMP (default) or REPEAT


Updated on November 12, 2021 11:30:58am UTC

