Py5MouseEvent.get_x()
=====================

Return the x position of the mouse at the time of this mouse event.

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

Return the x position of the mouse at the time of this mouse event. This information can also be obtained with :doc:`sketch_mouse_x`.

Underlying Processing method: getX

Signatures
------

.. code:: python

    get_x() -> int
Updated on August 25, 2022 20:01:47pm UTC

