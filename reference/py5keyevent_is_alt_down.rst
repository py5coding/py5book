Py5KeyEvent.is_alt_down()
=========================

Return boolean value reflecting if the Alt key is down.

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


    def key_pressed(e):
        if e.is_alt_down():
            py5.println('the alt key is down')
        else:
            py5.println('the alt key is not down')

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Return boolean value reflecting if the Alt key is down. The Alt key is a modifier key and can be pressed at the same time as other keys.

Underlying Processing method: isAltDown

Syntax
------

.. code:: python

    is_alt_down() -> bool

Updated on April 27, 2022 10:44:51am UTC

