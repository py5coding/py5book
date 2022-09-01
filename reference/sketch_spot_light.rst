spot_light()
============

Adds a spot light.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_spot_light_0.png
    :alt: example picture for spot_light()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.background(0)
        py5.no_stroke()
        py5.spot_light(51, 102, 126, 80, 20, 40, -1, 0, 0, py5.PI/2, 2)
        py5.translate(20, 50, 0)
        py5.sphere(30)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_spot_light_1.png
    :alt: example picture for spot_light()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        concentration = 600  # try 1 -> 10000
        py5.background(0)
        py5.no_stroke()
        py5.spot_light(51, 102, 126, 50, 50, 400,
                       0, 0, -1, py5.PI/16, concentration)
        py5.translate(80, 50, 0)
        py5.sphere(30)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Adds a spot light. Lights need to be included in the ``draw()`` to remain persistent in a looping program. Placing them in the ``setup()`` of a looping program will cause them to only have an effect the first time through the loop. The ``v1``, ``v2``, and ``v3`` parameters are interpreted as either RGB or HSB values, depending on the current color mode. The ``x``, ``y``, and ``z`` parameters specify the position of the light and ``nx``, ``ny``, ``nz`` specify the direction of light. The ``angle`` parameter affects angle of the spotlight cone, while ``concentration`` sets the bias of light focusing toward the center of that cone.

Underlying Processing method: `spotLight <https://processing.org/reference/spotLight_.html>`_

Signatures
----------

.. code:: python

    spot_light(
        v1: float,  # red or hue value (depending on current color mode)
        v2: float,  # green or saturation value (depending on current color mode)
        v3: float,  # blue or brightness value (depending on current color mode)
        x: float,  # x-coordinate of the light
        y: float,  # y-coordinate of the light
        z: float,  # z-coordinate of the light
        nx: float,  # direction along the x axis
        ny: float,  # direction along the y axis
        nz: float,  # direction along the z axis
        angle: float,  # angle of the spotlight cone
        concentration: float,  # exponent determining the center bias of the cone
        /,
    ) -> None

Updated on September 01, 2022 14:08:27pm UTC

