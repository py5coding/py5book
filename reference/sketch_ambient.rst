ambient()
=========

Sets the ambient reflectance for shapes drawn to the screen.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_ambient_0.png
    :alt: example picture for ambient()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.background(0)
        py5.no_stroke()
        py5.directional_light(153, 153, 153, .5, 0, -1)
        py5.ambient_light(153, 102, 0)
        py5.ambient(51, 26, 0)
        py5.translate(70, 50, 0)
        py5.sphere(30)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets the ambient reflectance for shapes drawn to the screen. This is combined with the ambient light component of the environment. The color components set through the parameters define the reflectance. For example in the default color mode, setting ``ambient(255, 127, 0)``, would cause all the red light to reflect and half of the green light to reflect. Use in combination with :doc:`sketch_emissive`, :doc:`sketch_specular`, and :doc:`sketch_shininess` to set the material properties of shapes.

Underlying Java method: `ambient <https://processing.org/reference/ambient_.html>`_

Syntax
------

.. code:: python

    ambient(gray: float, /) -> None
    ambient(rgb: int, /) -> None
    ambient(v1: float, v2: float, v3: float, /) -> None

Parameters
----------

* **gray**: `float` - number specifying value between white and black
* **rgb**: `int` - any value of the color datatype
* **v1**: `float` - red or hue value (depending on current color mode)
* **v2**: `float` - green or saturation value (depending on current color mode)
* **v3**: `float` - blue or brightness value (depending on current color mode)


Updated on September 11, 2021 16:51:34pm UTC

