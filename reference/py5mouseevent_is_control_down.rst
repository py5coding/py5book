Py5MouseEvent.is_control_down()
===============================

Return boolean value reflecting if the Control key is down.

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
        py5.size(200, 200)
        py5.rect_mode(py5.CENTER)


    def draw():
        py5.square(py5.random(py5.width), py5.random(py5.height), 10)


    def mouse_clicked(e):
        if e.is_control_down():
            py5.println('the control key is down')
        else:
            py5.println('the control key is not down')

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Return boolean value reflecting if the Control key is down. The Control key is a modifier key and can be pressed at the same time as other keys.

Underlying Processing method: isControlDown

Syntax
------

.. code:: python

    is_control_down() -> bool

Updated on April 27, 2022 10:44:51am UTC

