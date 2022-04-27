Py5KeyEvent
===========

Datatype for providing information about key events.

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

Datatype for providing information about key events. An instance of this class will be passed to user-defined key event functions if py5 detects those functions accept 1 (positional) argument, as demonstrated in the example code. The key event functions can be any of ``key_pressed()``, ``key_typed()``, or ``key_released()``. Key events can be generated faster than the frame rate of the Sketch, making key event functions useful for capturing all of a user's keyboard activity.

Underlying Processing class: KeyEvent

The following methods and fields are provided:

.. include:: include_py5keyevent.rst

Updated on April 27, 2022 10:44:51am UTC

