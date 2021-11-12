directional_light()
===================

Adds a directional light.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_directional_light_0.png
    :alt: example picture for directional_light()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.background(0)
        py5.no_stroke()
        py5.directional_light(51, 102, 126, -1, 0, 0)
        py5.translate(20, 50, 0)
        py5.sphere(30)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_directional_light_1.png
    :alt: example picture for directional_light()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.background(0)
        py5.no_stroke()
        py5.directional_light(51, 102, 126, 0, -1, 0)
        py5.translate(80, 50, 0)
        py5.sphere(30)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Adds a directional light. Directional light comes from one direction: it is stronger when hitting a surface squarely, and weaker if it hits at a gentle angle. After hitting a surface, directional light scatters in all directions. Lights need to be included in the ``draw()`` to remain persistent in a looping program. Placing them in the ``setup()`` of a looping program will cause them to only have an effect the first time through the loop. The ``v1``, ``v2``, and ``v3`` parameters are interpreted as either ``RGB`` or ``HSB`` values, depending on the current color mode. The ``nx``, ``ny``, and ``nz`` parameters specify the direction the light is facing. For example, setting ``ny`` to -1 will cause the geometry to be lit from below (since the light would be facing directly upward).

Underlying Processing method: `directionalLight <https://processing.org/reference/directionalLight_.html>`_

Syntax
------

.. code:: python

    directional_light(v1: float, v2: float, v3: float, nx: float, ny: float, nz: float, /) -> None

Parameters
----------

* **nx**: `float` - direction along the x-axis
* **ny**: `float` - direction along the y-axis
* **nz**: `float` - direction along the z-axis
* **v1**: `float` - red or hue value (depending on current color mode)
* **v2**: `float` - green or saturation value (depending on current color mode)
* **v3**: `float` - blue or brightness value (depending on current color mode)


Updated on November 12, 2021 11:30:58am UTC

