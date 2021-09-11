Py5Surface.set_icon()
=====================

Set the Sketch window icon.

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

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def settings():
        py5.size(200, 200, py5.P2D)
        PJOGL = py5.JClass("processing.opengl.PJOGL")
        PJOGL.setIcon("data/logo-64x64.png")


    def setup():
        surface = py5.get_surface()
        surface.set_title("py5 window")
        surface.set_always_on_top(True)


    py5.run_sketch(block=False)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Set the Sketch window icon. This will typically appear in the window's title bar. The default window icon is the same as Processing's.

This method will not work for the ``P2D`` or ``P3D`` renderers. Setting the icon for those renderers is a bit tricky; the icon must be a PNG file and it must be done in ``settings()``. See the second example to learn how to do that.

Underlying Java method: PSurface.setIcon

Syntax
------

.. code:: python

    set_icon(icon: Py5Image, /) -> None

Parameters
----------

* **icon**: `Py5Image` - image to use as the window icon


Updated on September 11, 2021 16:51:34pm UTC

