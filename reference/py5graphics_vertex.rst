Py5Graphics.vertex()
====================

Add a new vertex to a shape.

Description
-----------

Add a new vertex to a shape. All shapes are constructed by connecting a series of vertices. The ``vertex()`` method is used to specify the vertex coordinates for points, lines, triangles, quads, and polygons. It is used exclusively within the :doc:`py5graphics_begin_shape` and :doc:`py5graphics_end_shape` functions.

Drawing a vertex in 3D using the ``z`` parameter requires the ``P3D`` renderer.

This method is also used to map a texture onto geometry. The :doc:`py5graphics_texture` function declares the texture to apply to the geometry and the ``u`` and ``v`` coordinates define the mapping of this texture to the form. By default, the coordinates used for ``u`` and ``v`` are specified in relation to the image's size in pixels, but this relation can be changed with the :doc:`py5graphics_texture_mode` method.

This method is the same as :doc:`sketch_vertex` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_vertex`.

Underlying Java method: PGraphics.vertex

Syntax
------

.. code:: python

    vertex(v: NDArray[(Any,), Float], /) -> None
    vertex(x: float, y: float, /) -> None
    vertex(x: float, y: float, u: float, v: float, /) -> None
    vertex(x: float, y: float, z: float, /) -> None
    vertex(x: float, y: float, z: float, u: float, v: float, /) -> None

Parameters
----------

* **u**: `float` - horizontal coordinate for the texture mapping
* **v**: `NDArray[(Any,), Float]` - vertical coordinate for the texture mapping
* **v**: `float` - vertical coordinate for the texture mapping
* **x**: `float` - x-coordinate of the vertex
* **y**: `float` - y-coordinate of the vertex
* **z**: `float` - z-coordinate of the vertex


Updated on September 11, 2021 16:51:34pm UTC

