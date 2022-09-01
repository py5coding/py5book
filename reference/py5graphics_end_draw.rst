Py5Graphics.end_draw()
======================

Finalizes the rendering of a ``Py5Graphics`` object so that it can be shown on screen.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global pg
        py5.size(200, 200, py5.P2D)
        pg = py5.create_graphics(80, 80, py5.P2D)
        pg.begin_draw()
        pg.background(102)
        pg.stroke(255)
        pg.line(20, 20, 80, 80)
        pg.end_draw()


    def draw():
        py5.image(pg, 10, 10)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Finalizes the rendering of a ``Py5Graphics`` object so that it can be shown on screen.

Underlying Processing method: `PGraphics.endDraw <https://processing.org/reference/PGraphics_endDraw_.html>`_

Signatures
----------

.. code:: python

    end_draw() -> None

Updated on September 01, 2022 14:08:27pm UTC

