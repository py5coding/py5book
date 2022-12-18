Py5MouseEvent.get_y()
=====================

Return the y position of the mouse at the time of this mouse event.

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
        py5.rect_mode(py5.CENTER)


    def draw():
        py5.square(py5.random(py5.width), py5.random(py5.height), 10)


    def mouse_clicked(e):
        py5.println(e.get_x(), e.get_y())

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Return the y position of the mouse at the time of this mouse event. This information can also be obtained with :doc:`sketch_mouse_y`.

Underlying Processing method: getY

Signatures
----------

.. code:: python

    get_y() -> int

Updated on September 01, 2022 16:36:02pm UTC

