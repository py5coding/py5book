Py5Graphics.texture()
=====================

Sets a texture to be applied to vertex points.

Description
-----------

Sets a texture to be applied to vertex points. The ``texture()`` method must be called between :doc:`py5graphics_begin_shape` and :doc:`py5graphics_end_shape` and before any calls to :doc:`py5graphics_vertex`. This method only works with the ``P2D`` and ``P3D`` renderers.

When textures are in use, the fill color is ignored. Instead, use :doc:`py5graphics_tint` to specify the color of the texture as it is applied to the shape.

This method is the same as :doc:`sketch_texture` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_texture`.

Underlying Processing method: PGraphics.texture

Syntax
------

.. code:: python

    texture(image: Py5Image, /) -> None

Parameters
----------

* **image**: `Py5Image` - reference to a Py5Image object


Updated on November 12, 2021 11:30:58am UTC

