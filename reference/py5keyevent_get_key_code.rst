Py5KeyEvent.get_key_code()
==========================

Return the key code for the key event.

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


    def key_pressed(e):
        msgs = []
        if e.get_key() == py5.CODED:
            key_code = e.get_key_code()
            if key_code == py5.UP:
                py5.println('UP')
            if key_code == py5.LEFT:
                py5.println('LEFT')
            if key_code == py5.RIGHT:
                py5.println('RIGHT')
            if key_code == py5.DOWN:
                py5.println('DOWN')

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Return the key code for the key event. This method is important for key events involving coded keys such as the arrow or modifier keys. This information can also be obtained with :doc:`sketch_key_code`.

Underlying Processing method: getKeyCode

Signatures
------

.. code:: python

    get_key_code() -> int
Updated on August 25, 2022 20:01:47pm UTC

