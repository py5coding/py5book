Py5KeyEvent.is_meta_down()
==========================

Return boolean value reflecting if the Meta key is down.

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
        if e.is_meta_down():
            py5.println('the meta key is down')
        else:
            py5.println('the meta key is not down')

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Return boolean value reflecting if the Meta key is down. The Meta key is a modifier key and can be pressed at the same time as other keys.

Underlying Processing method: isMetaDown

Signatures
----------

.. code:: python

    is_meta_down() -> bool
Updated on September 01, 2022 12:53:02pm UTC

