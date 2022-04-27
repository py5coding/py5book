Py5MouseEvent
=============

Datatype for providing information about mouse events.

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
        py5.println('mouse clicked: ' + (','.join(msgs) if msgs else 'no modifiers'))

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


    def mouse_clicked(e):
        py5.println('mouse click count:', e.get_count())

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Datatype for providing information about mouse events. An instance of this class will be passed to user-defined mouse event functions if py5 detects those functions accept 1 (positional) argument, as demonstrated in the example code. The mouse event functions can be any of ``mouse_clicked()``, ``mouse_dragged()``, ``mouse_moved()``, ``mouse_entered()``, ``mouse_exited()``, ``mouse_pressed()``, ``mouse_released()``, or ``mouse_wheel()``. Mouse events can be generated faster than the frame rate of the Sketch, making mouse event functions useful for capturing all of a user's mouse activity.

Underlying Processing class: MouseEvent

The following methods and fields are provided:

.. include:: include_py5mouseevent.rst

Updated on April 27, 2022 10:44:51am UTC

