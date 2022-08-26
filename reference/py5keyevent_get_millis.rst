Py5KeyEvent.get_millis()
========================

Return the event's timestamp.

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
        py5.println('key event time:', e.get_millis())

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Return the event's timestamp. This will be measured in milliseconds.

Underlying Processing method: getMillis

Signatures
------

.. code:: python

    get_millis() -> int
Updated on August 25, 2022 20:01:47pm UTC

