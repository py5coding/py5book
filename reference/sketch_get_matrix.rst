get_matrix()
============

Get the current matrix as a numpy array.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_get_matrix_0.png
    :alt: example picture for get_matrix()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.no_fill()
        py5.translate(50, 50, 0)
        py5.rotate_y(py5.PI/6)
        global matrix
        matrix = py5.get_matrix()
        py5.println(matrix)
        py5.println(matrix.dtype)
        py5.stroke(153)
        py5.box(50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Get the current matrix as a numpy array. Use the ``target`` parameter to put the matrix data in a properly sized and typed numpy array.

Underlying Processing method: getMatrix

Syntax
------

.. code:: python

    get_matrix() -> NDArray[(Any, Any), Float]
    get_matrix(target: NDArray[(2, 3), Float], /) -> NDArray[(2, 3), Float]
    get_matrix(target: NDArray[(4, 4), Float], /) -> NDArray[(4, 4), Float]

Parameters
----------

* **target**: `NDArray[(2, 3), Float]` - transformation matrix data
* **target**: `NDArray[(4, 4), Float]` - transformation matrix data


Updated on November 12, 2021 11:30:58am UTC

