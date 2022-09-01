Py5Vector.set_limit()
=====================

Constrain the vector's magnitude to a specified value.

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

    def draw():
        py5.background(128)
        py5.translate(py5.width / 2, py5.height / 2)
        v1 = py5.Py5Vector(py5.mouse_x - py5.width / 2, py5.mouse_y - py5.height / 2)

        py5.stroke(0)
        py5.stroke_weight(5)
        py5.line(0, 0, v1.x, v1.y)

        v1.set_limit(25)

        py5.stroke(255, 0, 0)
        py5.stroke_weight(2)
        py5.line(0, 0, v1.x, v1.y)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Constrain the vector's magnitude to a specified value. If the vector's magnitude is already less than or equal to ``max_mag``, this method will have no effect. If the vector's magnitude is larger, it will be set to ``max_mag``. The ``max_mag`` parameter cannot be a negative number.

Signatures
----------

.. code:: python

    set_limit(
        max_mag: float,  # maximum vector magnitude
    ) -> Py5Vector

Updated on September 01, 2022 14:08:27pm UTC

