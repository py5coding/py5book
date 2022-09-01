Py5KeyEvent.get_key()
=====================

Return the key for the key event.

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
        pressed_key = e.get_key()
        if pressed_key != py5.CODED:
            py5.println(f'the {pressed_key} key was pressed')

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Return the key for the key event. If the value is ``CODED``, use :doc:`py5keyevent_get_key_code` instead. This information can also be obtained with :doc:`sketch_key`.

Underlying Processing method: getKey

Signatures
----------

.. code:: python

    get_key() -> chr
Updated on September 01, 2022 12:53:02pm UTC

