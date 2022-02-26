set_matrix()
============

Set the current matrix to the one specified through the parameter ``source``.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_set_matrix_0.png
    :alt: example picture for set_matrix()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    import numpy as np


    def setup():
        py5.size(100, 100, py5.P3D)
        py5.no_fill()
        matrix = np.array([[0.866025, 0, 0.5, 0],
                           [0, 1, 0, 0],
                           [-0.5, 0, 0.866025, -86.6025],
                           [0, 0, 0, 1]], dtype=np.float64)
        py5.set_matrix(matrix)
        py5.stroke(153)
        py5.box(50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Set the current matrix to the one specified through the parameter ``source``. Inside the Processing code it will call :doc:`sketch_reset_matrix` followed by :doc:`sketch_apply_matrix`. This will be very slow because :doc:`sketch_apply_matrix` will try to calculate the inverse of the transform, so avoid it whenever possible.

Underlying Processing method: setMatrix

Syntax
------

.. code:: python

    set_matrix(source: npt.NDArray[np.floating], /) -> None

Parameters
----------

* **source**: `npt.NDArray[np.floating]` - transformation matrix with a shape of 2x3 for 2D transforms or 4x4 for 3D transforms


Updated on February 26, 2022 13:22:44pm UTC

