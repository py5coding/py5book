clip()
======

Limits the rendering to the boundaries of a rectangle defined by the parameters.

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
        py5.size(200, 200)
        py5.image_mode(py5.CENTER)


    def draw():
        py5.background(204)
        if py5.is_mouse_pressed:
            py5.clip(py5.mouse_x, py5.mouse_y, 100, 100)
        else:
            py5.no_clip()

        py5.line(0, 0, py5.width, py5.height)
        py5.line(0, py5.height, py5.width, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Limits the rendering to the boundaries of a rectangle defined by the parameters. The boundaries are drawn based on the state of the :doc:`sketch_image_mode` fuction, either ``CORNER``, ``CORNERS``, or ``CENTER``.

Underlying Processing method: `clip <https://processing.org/reference/clip_.html>`_

Signatures
----------

.. code:: python

    clip(
        a: float,  # x-coordinate of the rectangle, by default
        b: float,  # y-coordinate of the rectangle, by default
        c: float,  # width of the rectangle, by default
        d: float,  # height of the rectangle, by default
        /,
    ) -> None
Updated on September 01, 2022 12:53:02pm UTC

