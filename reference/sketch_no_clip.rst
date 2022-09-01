no_clip()
=========

Disables the clipping previously started by the :doc:`sketch_clip` function.

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

Disables the clipping previously started by the :doc:`sketch_clip` function.

Underlying Processing method: `noClip <https://processing.org/reference/noClip_.html>`_

Signatures
----------

.. code:: python

    no_clip() -> None

Updated on September 01, 2022 16:36:02pm UTC

