Py5Surface.set_title()
======================

Set the Sketch window's title.

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

Set the Sketch window's title. This will typically appear at the window's title bar. The default window title is "Sketch".

Underlying Processing method: PSurface.setTitle

Syntax
------

.. code:: python

    set_title(title: str, /) -> None

Parameters
----------

* **title**: `str` - new window title


Updated on May 02, 2022 12:07:22pm UTC

