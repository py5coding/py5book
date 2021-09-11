ambient_light()
===============

Adds an ambient light.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_ambient_light_0.png
    :alt: example picture for ambient_light()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.background(0)
        py5.no_stroke()
        # the spheres are white by default so
        # the ambient light changes their color
        py5.ambient_light(51, 102, 126)
        py5.translate(20, 50, 0)
        py5.sphere(30)
        py5.translate(60, 0, 0)
        py5.sphere(30)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_ambient_light_1.png
    :alt: example picture for ambient_light()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.background(0)
        py5.no_stroke()
        py5.directional_light(126, 126, 126, 0, 0, -1)
        py5.ambient_light(102, 102, 102)
        py5.translate(32, 50, 0)
        py5.rotate_y(py5.PI/5)
        py5.box(40)
        py5.translate(60, 0, 0)
        py5.sphere(30)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Adds an ambient light. Ambient light doesn't come from a specific direction, the rays of light have bounced around so much that objects are evenly lit from all sides. Ambient lights are almost always used in combination with other types of lights. Lights need to be included in the ``draw()`` to remain persistent in a looping program. Placing them in the ``setup()`` of a looping program will cause them to only have an effect the first time through the loop. The ``v1``, ``v2``, and ``v3`` parameters are interpreted as either ``RGB`` or ``HSB`` values, depending on the current color mode.

Underlying Java method: `ambientLight <https://processing.org/reference/ambientLight_.html>`_

Syntax
------

.. code:: python

    ambient_light(v1: float, v2: float, v3: float, /) -> None
    ambient_light(v1: float, v2: float, v3: float, x: float, y: float, z: float, /) -> None

Parameters
----------

* **v1**: `float` - red or hue value (depending on current color mode)
* **v2**: `float` - green or saturation value (depending on current color mode)
* **v3**: `float` - blue or brightness value (depending on current color mode)
* **x**: `float` - x-coordinate of the light
* **y**: `float` - y-coordinate of the light
* **z**: `float` - z-coordinate of the light


Updated on September 11, 2021 16:51:34pm UTC

