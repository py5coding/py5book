Py5Surface.set_always_on_top()
==============================

Set the Sketch window to always be on top of other windows.

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
        surface.set_title("py5 window")
        surface.set_always_on_top(True)
        surface.set_icon(py5.load_image("logo-64x64.png"))

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Set the Sketch window to always be on top of other windows. By default, the Sketch window can be covered by other windows. Setting this to ``True`` will keep that from happening.

Underlying Processing method: PSurface.setAlwaysOnTop

Syntax
------

.. code:: python

    set_always_on_top(always: bool, /) -> None

Parameters
----------

* **always**: `bool` - should the Sketch window always be on top of other windows


Updated on November 12, 2021 11:30:58am UTC

