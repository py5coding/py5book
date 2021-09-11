light_falloff()
===============

Sets the falloff rates for point lights, spot lights, and ambient lights.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_light_falloff_0.png
    :alt: example picture for light_falloff()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.no_stroke()
        py5.background(0)
        py5.light_falloff(1.0, 0.001, 0.0)
        py5.point_light(150, 250, 150, 50, 50, 50)
        py5.begin_shape()
        py5.vertex(0, 0, 0)
        py5.vertex(100, 0, -100)
        py5.vertex(100, 100, -100)
        py5.vertex(0, 100, 0)
        py5.end_shape(py5.CLOSE)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets the falloff rates for point lights, spot lights, and ambient lights. Like :doc:`sketch_fill`, it affects only the elements which are created after it in the code. The default value is ``light_falloff(1.0, 0.0, 0.0)``, and the parameters are used to calculate the falloff with the equation ``falloff = 1 / (CONSTANT + d * ``LINEAR`` + (d*d) * QUADRATIC)``, where ``d`` is the distance from light position to vertex position.

Thinking about an ambient light with a falloff can be tricky. If you want a region of your scene to be lit ambiently with one color and another region to be lit ambiently with another color, you could use an ambient light with location and falloff. You can think of it as a point light that doesn't care which direction a surface is facing.

Underlying Java method: `lightFalloff <https://processing.org/reference/lightFalloff_.html>`_

Syntax
------

.. code:: python

    light_falloff(constant: float, linear: float, quadratic: float, /) -> None

Parameters
----------

* **constant**: `float` - constant value or determining falloff
* **linear**: `float` - linear value for determining falloff
* **quadratic**: `float` - quadratic value for determining falloff


Updated on September 11, 2021 16:51:34pm UTC

