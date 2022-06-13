Py5Vector.angle_between()
=========================

Measure the angle between two vectors.

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

.. image:: /images/reference/Py5Vector_angle_between_0.png
    :alt: example picture for angle_between()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.translate(20, 20)
        v1 = py5.Py5Vector(60, 0)
        v2 = py5.Py5Vector(45, 45)
        py5.line(0, 0, v1.x, v1.y)
        py5.line(0, 0, v2.x, v2.y)
        angle_radians = v1.angle_between(v2)
        py5.no_fill()
        py5.arc(0, 0, 40, 40, 0, angle_radians)
        py5.fill(0)
        py5.text(f'{round(py5.degrees(angle_radians))}°', 25, 15)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Measure the angle between two vectors.

Syntax
------

.. code:: python

    angle_between(other: Union[Py5Vector, np.ndarray]) -> Union[float, np.ndarray[np.floating]]

Parameters
----------

* **other**: `Union[Py5Vector, np.ndarray]` - vector to measure angle between


Updated on June 13, 2022 01:23:16am UTC

