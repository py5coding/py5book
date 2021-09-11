Py5Graphics.begin_raw()
=======================

To create vectors from 3D data, use the ``begin_raw()`` and :doc:`py5graphics_end_raw` commands.

Description
-----------

To create vectors from 3D data, use the ``begin_raw()`` and :doc:`py5graphics_end_raw` commands. These commands will grab the shape data just before it is rendered to the ``Py5Graphics`` object. At this stage, the ``Py5Graphics`` object contains nothing but a long list of individual lines and triangles. This means that a shape created with :doc:`py5graphics_sphere` function will be made up of hundreds of triangles, rather than a single object. Or that a multi-segment line shape (such as a curve) will be rendered as individual segments.

When using ``begin_raw()`` and :doc:`py5graphics_end_raw`, it's possible to write to either a 2D or 3D renderer. For instance, ``begin_raw()`` with the ``PDF`` library will write the geometry as flattened triangles and lines, even if recording from the ``P3D`` renderer. 

If you want a background to show up in your files, use ``rect(0, 0, width, height)`` after setting the :doc:`py5graphics_fill` to the background color. Otherwise the background will not be rendered to the file because the background is not shape.

Using ``hint(ENABLE_DEPTH_SORT)`` can improve the appearance of 3D geometry drawn to 2D file formats.

This method is the same as :doc:`sketch_begin_raw` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_begin_raw`.

Underlying Java method: PGraphics.beginRaw

Syntax
------

.. code:: python

    begin_raw(raw_graphics: Py5Graphics, /) -> None

Parameters
----------

* **raw_graphics**: `Py5Graphics` - Py5Graphics object to apply draw commands to


Updated on September 11, 2021 16:51:34pm UTC

