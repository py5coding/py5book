Py5Graphics.quadratic_vertices()
================================

Create a collection of quadratic vertices.

Description
-----------

Create a collection of quadratic vertices. The purpose of this method is to provide an alternative to repeatedly calling :doc:`py5graphics_quadratic_vertex` in a loop. For a large number of quadratic vertices, the performance of ``quadratic_vertices()`` will be much faster.

The ``coordinates`` parameter should be a numpy array with one row for each quadratic vertex. The first few columns are for the control point and the next few columns are for the anchor point. There should be four or six columns for 2D or 3D points, respectively.

This method is the same as :doc:`sketch_quadratic_vertices` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_quadratic_vertices`.

Underlying Processing method: PGraphics.quadraticVertices

Syntax
------

.. code:: python

    quadratic_vertices(coordinates: npt.NDArray[np.floating], /) -> None

Parameters
----------

* **coordinates**: `npt.NDArray[np.floating]` - 2D array of quadratic vertex coordinates with 4 or 6 columns for 2D or 3D points, respectively


Updated on February 26, 2022 13:22:44pm UTC

