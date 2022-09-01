Py5KeyEvent.is_auto_repeat()
============================

Identifies if the pressed key is auto repeating, as faciliated by the computer's operating system.

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
        if e.is_auto_repeat():
            py5.println('key press is auto repeating')
        else:
            py5.println('key press is not auto repeating')

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Identifies if the pressed key is auto repeating, as faciliated by the computer's operating system. This method might work differently (or not at all) depending on the renderer used by the Sketch and the operating system the Sketch is run on.

Underlying Processing method: isAutoRepeat

Signatures
----------

.. code:: python

    is_auto_repeat() -> bool
Updated on September 01, 2022 12:53:02pm UTC

