points()
========

Draw a collection of points, each a coordinate in space at the dimension of one pixel.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_points_0.png
    :alt: example picture for points()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    import numpy as np

    def setup():
        random_points = 100 * np.random.rand(500, 2)
        py5.points(random_points)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Draw a collection of points, each a coordinate in space at the dimension of one pixel. The purpose of this method is to provide an alternative to repeatedly calling :doc:`sketch_point` in a loop. For a large number of points, the performance of ``points()`` will be much faster.

The ``coordinates`` parameter should be a numpy array with one row for each point. There should be two or three columns for 2D or 3D points, respectively.

Underlying Processing method: points

Signatures
----------

.. code:: python

    points(
        coordinates: npt.NDArray[np.floating],  # 2D array of point coordinates with 2 or 3 columns for 2D or 3D points, respectively
        /,
    ) -> None

Updated on September 01, 2022 16:36:02pm UTC

