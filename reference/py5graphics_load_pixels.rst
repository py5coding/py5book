Py5Graphics.load_pixels()
=========================

Loads the pixel data of the current Py5Graphics drawing surface into the :doc:`py5graphics_pixels` array.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Graphics_load_pixels_0.png
    :alt: example picture for load_pixels()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        g = py5.create_graphics(60, 60)
        g.begin_draw()
        g.background(255, 0, 0)
        g.rect(10, 10, 40, 40)
        g.load_pixels()
        yellow = "#FF0"
        for i in range(len(g.pixels) // 2):
            g.pixels[i] = yellow
        g.update_pixels()
        g.end_draw()

        py5.background(240)
        py5.image(g, 20, 20)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Loads the pixel data of the current Py5Graphics drawing surface into the :doc:`py5graphics_pixels` array. This function must always be called before reading from or writing to :doc:`py5graphics_pixels`. Subsequent changes to the Py5Graphics drawing surface will not be reflected in :doc:`py5graphics_pixels` until ``load_pixels()`` is called again.

This method is the same as :doc:`sketch_load_pixels` but linked to a ``Py5Graphics`` object.

Underlying Processing method: PGraphics.loadPixels

Signatures
----------

.. code:: python

    load_pixels() -> None
Updated on September 01, 2022 12:53:02pm UTC

