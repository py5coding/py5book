Py5KeyEvent.get_action()
========================

Return the key event's action.

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
        py5.println('key pressed:', e.get_action() == e.PRESS)


    def key_released(e):
        py5.println('key released:', e.get_action() == e.RELEASE)


    def key_typed(e):
        py5.println('key typed:', e.get_action() == e.TYPE)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Return the key event's action. This value will always be implied by the triggered event function, but perhaps it might be useful to someone someday.

Underlying Processing method: getAction

Signatures
----------

.. code:: python

    get_action() -> int

Updated on September 01, 2022 14:08:27pm UTC

