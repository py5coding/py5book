Py5Graphics.begin_raw()
=======================

To create vectors from 3D data, use the ``begin_raw()`` and :doc:`py5graphics_end_raw` commands.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        py5.size(200, 200, py5.P2D)

        g = py5.create_graphics(100, 100, py5.P2D)
        g2 = py5.create_graphics(100, 100, py5.SVG, "/tmp/raw2.svg")

        with g.begin_draw():
            with g.begin_raw(g2):
                g.rect_mode(py5.CENTER)
                g.fill("#F00")
                for _ in range(10):
                    g.square(py5.random(g.width), py5.random(g.height), 10)

        py5.image(g, 10, 10)
        py5.image(g, 100, 100)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

To create vectors from 3D data, use the ``begin_raw()`` and :doc:`py5graphics_end_raw` commands. These commands will grab the shape data just before it is rendered to the ``Py5Graphics`` object. At this stage, the ``Py5Graphics`` object contains nothing but a long list of individual lines and triangles. This means that a shape created with :doc:`py5graphics_sphere` function will be made up of hundreds of triangles, rather than a single object. Or that a multi-segment line shape (such as a curve) will be rendered as individual segments.

When using ``begin_raw()`` and :doc:`py5graphics_end_raw`, it's possible to write to either a 2D or 3D renderer. For instance, ``begin_raw()`` with the ``PDF`` library will write the geometry as flattened triangles and lines, even if recording from the ``P3D`` renderer. 

If you want a background to show up in your files, use ``rect(0, 0, width, height)`` after setting the :doc:`py5graphics_fill` to the background color. Otherwise the background will not be rendered to the file because the background is not a shape.

This method can be used as a context manager to ensure that :doc:`py5graphics_end_raw` always gets called, as shown in the example.

Using ``hint(ENABLE_DEPTH_SORT)`` can improve the appearance of 3D geometry drawn to 2D file formats.

This method is the same as :doc:`sketch_begin_raw` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_begin_raw`.

Underlying Processing method: PGraphics.beginRaw

Signatures
----------

.. code:: python

    begin_raw(
        raw_graphics: Py5Graphics,  # Py5Graphics object to apply draw commands to
        /,
    ) -> None

Updated on September 01, 2022 16:36:02pm UTC

