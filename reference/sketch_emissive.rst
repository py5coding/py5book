emissive()
==========

Sets the emissive color of the material used for drawing shapes drawn to the screen.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_emissive_0.png
    :alt: example picture for emissive()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.background(0)
        py5.no_stroke()
        py5.background(0)
        py5.directional_light(204, 204, 204, .5, 0, -1)
        py5.emissive(0, 26, 51)
        py5.translate(70, 50, 0)
        py5.sphere(30)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets the emissive color of the material used for drawing shapes drawn to the screen. Use in combination with :doc:`sketch_ambient`, :doc:`sketch_specular`, and :doc:`sketch_shininess` to set the material properties of shapes.

Underlying Java method: `emissive <https://processing.org/reference/emissive_.html>`_

Syntax
------

.. code:: python

    emissive(gray: float, /) -> None
    emissive(rgb: int, /) -> None
    emissive(v1: float, v2: float, v3: float, /) -> None

Parameters
----------

* **gray**: `float` - value between black and white, by default 0 to 255
* **rgb**: `int` - color to set
* **v1**: `float` - red or hue value (depending on current color mode)
* **v2**: `float` - green or saturation value (depending on current color mode)
* **v3**: `float` - blue or brightness value (depending on current color mode)


Updated on September 11, 2021 16:51:34pm UTC

