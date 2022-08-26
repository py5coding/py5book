quadratic_vertices()
====================

Create a collection of quadratic vertices.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_quadratic_vertices_0.png
    :alt: example picture for quadratic_vertices()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    import numpy as np

    def setup():
        random_quadratic_vertices = 100 * np.random.rand(25, 4)
        py5.begin_shape()
        py5.vertex(py5.width / 2, py5.height / 2)
        py5.quadratic_vertices(random_quadratic_vertices)
        py5.end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Create a collection of quadratic vertices. The purpose of this method is to provide an alternative to repeatedly calling :doc:`sketch_quadratic_vertex` in a loop. For a large number of quadratic vertices, the performance of ``quadratic_vertices()`` will be much faster.

The ``coordinates`` parameter should be a numpy array with one row for each quadratic vertex. The first few columns are for the control point and the next few columns are for the anchor point. There should be four or six columns for 2D or 3D points, respectively.

Underlying Processing method: quadraticVertices

Signatures
------

.. code:: python

    quadratic_vertices(
        coordinates: npt.NDArray[np.floating],  # 2D array of quadratic vertex coordinates with 4 or 6 columns for 2D or 3D points, respectively
        /,
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

