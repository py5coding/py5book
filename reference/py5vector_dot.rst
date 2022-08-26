Py5Vector.dot()
===============

Calculate the dot product between two vectors.

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

    import numpy as np

    v1 = py5.Py5Vector(0, 40)
    v2 = py5.Py5Vector(10, 10)
    angle = v1.angle_between(v2)
    print(f'angle = {round(py5.degrees(angle))}°')
    # angle = 45°
    angle = np.arccos(v1.norm.dot(v2.norm))
    print(f'angle = {round(py5.degrees(angle))}°')
    # angle = 45°

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global v1
        v1 = py5.Py5Vector(40, 0)


    def draw():
        py5.background(255)
        py5.translate(py5.width / 2, py5.height / 2)
        py5.stroke(0)
        py5.stroke_weight(4)
        py5.line(0, 0, v1.x, v1.y)
        vm = py5.Py5Vector(py5.mouse_x - py5.width / 2, py5.mouse_y - py5.height / 2)
        py5.stroke_weight(2)
        py5.stroke(0, 255, 0)
        py5.line(0, 0, vm.x, vm.y)
        v2 = v1.norm.dot(vm) * v1.norm
        py5.stroke(255, 0, 0)
        py5.line(0, 0, v2.x, v2.y)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Calculate the dot product between two vectors.

Signatures
------

.. code:: python

    dot(
        other: Union[Py5Vector, np.ndarray]  # vector to calculate the dot product with
    ) -> Union[float, np.ndarray[np.floating]]
Updated on August 25, 2022 20:01:47pm UTC

