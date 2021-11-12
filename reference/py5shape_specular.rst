Py5Shape.specular()
===================

Sets the specular color of a ``Py5Shape`` object's material, which sets the color of highlight.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_specular_0.png
    :alt: example picture for specular()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def create_strip(r, g, b):
        s = py5.create_shape()
        s.begin_shape(py5.TRIANGLE_STRIP)
        s.fill(0, 51, 102)
        s.specular(r, g, b)
        s.vertex(10, 40, -25)
        s.vertex(20, 0, -10)
        s.vertex(30, 40, 0)
        s.vertex(40, 0, 5)
        s.vertex(50, 40, 0)
        s.vertex(60, 0, -10)
        s.vertex(70, 40, -25)
        s.end_shape()
        return s


    def setup():
        py5.size(100, 100, py5.P3D)
        py5.background(0)
        py5.light_specular(255, 255, 255)
        py5.directional_light(204, 204, 204, 0, 0, -1)
        py5.shape(create_strip(255, 255, 255), 0, 5)
        py5.shape(create_strip(204, 102, 0), 0, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets the specular color of a ``Py5Shape`` object's material, which sets the color of highlight. Specular refers to light which bounces off a surface in a preferred direction (rather than bouncing in all directions like a diffuse light). Use in combination with :doc:`py5shape_emissive`, :doc:`py5shape_ambient`, and :doc:`py5shape_shininess` to set the material properties of a ``Py5Shape`` object.

This method can only be used within a :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` pair. The specular color setting will be applied to vertices added after the call to this method.

Underlying Processing method: PShape.specular

Syntax
------

.. code:: python

    specular(gray: float, /) -> None
    specular(rgb: int, /) -> None
    specular(x: float, y: float, z: float, /) -> None

Parameters
----------

* **gray**: `float` - value between black and white, by default 0 to 255
* **rgb**: `int` - color to set
* **x**: `float` - red or hue value (depending on current color mode)
* **y**: `float` - green or saturation value (depending on current color mode)
* **z**: `float` - blue or brightness value (depending on current color mode)


Updated on November 12, 2021 11:30:58am UTC

