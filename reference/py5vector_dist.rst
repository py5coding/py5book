Py5Vector.dist()
================

Calculate the distance between two vectors.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Vector_dist_0.png
    :alt: example picture for dist()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.background(128)
        v1 = py5.Py5Vector(22.8, 31.4)
        v2 = py5.Py5Vector(87.2, 72.4)
        py5.line(v1.x, v1.y, v2.x, v2.y)
        py5.text(f'dist = {v1.dist(v2):.2f}', 5, 15)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Calculate the distance between two vectors.

Signatures
----------

.. code:: python

    dist(
        other: Union[Py5Vector, np.ndarray]  # vector to calculate the distance from
    ) -> Union[float, np.ndarray[np.floating]]
Updated on September 01, 2022 12:53:02pm UTC

