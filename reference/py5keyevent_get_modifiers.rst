Py5KeyEvent.get_modifiers()
===========================

Integer value used to identify which modifier keys (if any) are currently pressed.

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


    def key_pressed(e):
        modifiers = e.get_modifiers()
        msgs = []
        if modifiers & e.SHIFT:
            msgs.append('shift is down')
        if modifiers & e.CTRL:
            msgs.append('control is down')
        if modifiers & e.META:
            msgs.append('meta is down')
        if modifiers & e.ALT:
            msgs.append('alt is down')
        py5.println('key pressed: ' + (', '.join(msgs) if msgs else 'no modifiers'))

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Integer value used to identify which modifier keys (if any) are currently pressed. Information about the modifier keys is encoded in the integer value and can be parsed with bit masking, as shown in the example.

Underlying Processing method: getModifiers

Signatures
----------

.. code:: python

    get_modifiers() -> int

Updated on September 01, 2022 16:36:02pm UTC

