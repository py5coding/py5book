Py5MouseEvent.get_button()
==========================

Identify the mouse button used in the event.

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
        mouse_button = e.get_button()
        if mouse_button == py5.LEFT:
            py5.println('left mouse click')
        elif mouse_button == py5.CENTER:
            py5.println('center mouse click')
        elif mouse_button == py5.RIGHT:
            py5.println('right mouse click')

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Identify the mouse button used in the event. This can be ``LEFT``, ``CENTER``, or ``RIGHT``.

Underlying Processing method: getButton

Signatures
------

.. code:: python

    get_button() -> int
Updated on August 25, 2022 20:01:47pm UTC

