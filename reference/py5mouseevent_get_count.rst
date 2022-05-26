Py5MouseEvent.get_count()
=========================

Get the number of mouse clicks.

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
        py5.println('mouse click count:', e.get_count())

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Get the number of mouse clicks. This will be 1 for a single mouse click and 2 for a double click. The value can be much higher if the user clicks fast enough.

Underlying Processing method: getCount

Syntax
------

.. code:: python

    get_count() -> int

Updated on April 27, 2022 10:44:51am UTC

