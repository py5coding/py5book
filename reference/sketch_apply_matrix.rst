apply_matrix()
==============

Multiplies the current matrix by the one specified through the parameters.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_apply_matrix_0.png
    :alt: example picture for apply_matrix()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.no_fill()
        py5.translate(50, 50, 0)
        py5.rotate_y(py5.PI/6)
        py5.stroke(153)
        py5.box(35)
        # set rotation angles
        ct = py5.cos(py5.PI/9.0)
        st = py5.sin(py5.PI/9.0)
        # matrix for rotation around the Y axis
        py5.apply_matrix(ct, 0.0, st, 0.0,
                         0.0, 1.0, 0.0, 0.0,
                         -st, 0.0, ct, 0.0,
                         0.0, 0.0, 0.0, 1.0)
        py5.stroke(255)
        py5.box(50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Multiplies the current matrix by the one specified through the parameters. This is very slow because it will try to calculate the inverse of the transform, so avoid it whenever possible. The equivalent function in OpenGL is ``gl_mult_matrix()``.

Underlying Processing method: `applyMatrix <https://processing.org/reference/applyMatrix_.html>`_

Syntax
------

.. code:: python

    apply_matrix(n00: float, n01: float, n02: float, n03: float, n10: float, n11: float, n12: float, n13: float, n20: float, n21: float, n22: float, n23: float, n30: float, n31: float, n32: float, n33: float, /) -> None
    apply_matrix(n00: float, n01: float, n02: float, n10: float, n11: float, n12: float, /) -> None
    apply_matrix(source: NDArray[(2, 3), Float], /) -> None
    apply_matrix(source: NDArray[(4, 4), Float], /) -> None

Parameters
----------

* **n00**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n01**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n02**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n03**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n10**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n11**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n12**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n13**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n20**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n21**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n22**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n23**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n30**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n31**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n32**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n33**: `float` - numbers which define the 4x4 matrix to be multiplied
* **source**: `NDArray[(2, 3), Float]` - 2D transformation matrix
* **source**: `NDArray[(4, 4), Float]` - 3D transformation matrix


Updated on November 12, 2021 11:30:58am UTC

