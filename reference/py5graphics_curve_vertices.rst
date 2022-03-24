Py5Graphics.curve_vertices()
============================

Create a collection of curve vertices.

Description
-----------

Create a collection of curve vertices. The purpose of this method is to provide an alternative to repeatedly calling :doc:`py5graphics_curve_vertex` in a loop. For a large number of curve vertices, the performance of ``curve_vertices()`` will be much faster.

The ``coordinates`` parameter should be a numpy array with one row for each curve vertex.  There should be two or three columns for 2D or 3D points, respectively.

This method is the same as :doc:`sketch_curve_vertices` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_curve_vertices`.

Underlying Processing method: PGraphics.curveVertices

Syntax
------

.. code:: python

    curve_vertices(coordinates: npt.NDArray[np.floating], /) -> None

Parameters
----------

* **coordinates**: `npt.NDArray[np.floating]` - 2D array of curve vertex coordinates with 2 or 3 columns for 2D or 3D points, respectively


Updated on February 26, 2022 13:22:44pm UTC

