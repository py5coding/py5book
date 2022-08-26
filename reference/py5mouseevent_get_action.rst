Py5MouseEvent.get_action()
==========================

Return the mouse event's action.

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


    def mouse_pressed(e):
        py5.println('mouse pressed:', e.get_action() == e.PRESS)


    def mouse_released(e):
        py5.println('mouse released:', e.get_action() == e.RELEASE)


    def mouse_clicked(e):
        py5.println('mouse clicked:', e.get_action() == e.CLICK)


    def mouse_dragged(e):
        py5.println('mouse dragged:', e.get_action() == e.DRAG)


    def mouse_moved(e):
        py5.println('mouse moved:', e.get_action() == e.MOVE)


    def mouse_entered(e):
        py5.println('mouse entered:', e.get_action() == e.ENTER)


    def mouse_exited(e):
        py5.println('mouse exited:', e.get_action() == e.EXIT)


    def mouse_wheel(e):
        py5.println('mouse wheel:', e.get_action() == e.WHEEL)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Return the mouse event's action. This value will always be implied by the triggered event function, but perhaps it might be useful to someone someday.

Underlying Processing method: getAction

Signatures
------

.. code:: python

    get_action() -> int
Updated on August 25, 2022 20:01:47pm UTC

