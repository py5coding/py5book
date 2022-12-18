Py5Graphics.clear()
===================

Clears the pixels within a buffer.

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
        global pg
        py5.size(200, 200)
        pg = py5.create_graphics(py5.width, py5.height)


    def draw():
        py5.background(204)

        # clear the Py5Graphics when the mouse is pressed
        if py5.is_mouse_pressed:
            pg.begin_draw()
            pg.clear()
            pg.end_draw()
        else:
            pg.begin_draw()
            pg.stroke(0, 102, 153)
            pg.line(py5.width//2, py5.height//2, py5.mouse_x, py5.mouse_y)
            pg.end_draw()

        py5.image(pg, 0, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Clears the pixels within a buffer. Unlike the main graphics context (the display window), pixels in ``Py5Graphics`` objects created with :doc:`sketch_create_graphics` can be entirely or partially transparent. This function clears everything in a ``Py5Graphics`` object to make all of the pixels 100% transparent.

Underlying Processing method: PGraphics.clear

Signatures
----------

.. code:: python

    clear() -> None

Updated on September 01, 2022 16:36:02pm UTC

