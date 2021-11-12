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

    set_matrix(source: NDArray[(2, 3), Float], /) -> None
    set_matrix(source: NDArray[(4, 4), Float], /) -> None

Parameters
----------

* **source**: `NDArray[(2, 3), Float]` - transformation matrix data
* **source**: `NDArray[(4, 4), Float]` - transformation matrix data


Updated on November 12, 2021 11:30:58am UTC

