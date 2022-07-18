Py5Surface.set_resizable()
==========================

Set the Sketch window as resizable by the user.

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
        surface = py5.get_surface()
        surface.set_resizable(True)


    def draw():
        py5.square(py5.random(py5.width), py5.random(py5.height), 10)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Set the Sketch window as resizable by the user. The user will be able to resize the window in the same way as they do for many other windows on their computer. By default, the Sketch window is not resizable.

Changing the window size will clear the drawing canvas. If you do this, the :doc:`sketch_width` and :doc:`sketch_height` variables will change.

This method provides the same functionality as :doc:`sketch_window_resizable`.

Underlying Processing method: PSurface.setResizable

Syntax
------

.. code:: python

    set_resizable(resizable: bool, /) -> None

Parameters
----------

* **resizable**: `bool` - should the Sketch window be resizable


Updated on July 18, 2022 17:22:20pm UTC

