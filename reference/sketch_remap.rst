remap()
=======

Re-maps a number from one range to another.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_remap_0.png
    :alt: example picture for remap()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(200, 200)
        value = 0.5
        # remap 0.5 to be half of the width
        m = py5.remap(value, 0, 1, 0, py5.width)
        py5.ellipse(m, 100, 10, 10)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        value = 110
        m = py5.remap(value, 0, 100, -20, -10)
        py5.println(m)  # Prints "-9.0"

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(200, 200)
        py5.no_stroke()


    def draw():
        py5.background(204)
        x1 = py5.remap(py5.mouse_x, 0, py5.width, 50, 150)
        py5.ellipse(x1, 75, 50, 50)
        x2 = py5.remap(py5.mouse_x, 0, py5.width, 0, 200)
        py5.ellipse(x2, 125, 50, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Re-maps a number from one range to another.

In the first example, the number 0.5 is converted from a value in the range of 0 to 1 into a value that ranges from the left edge of the window (0) to the right edge (:doc:`sketch_width`).

As shown in the second example, numbers outside of the range are not clamped to the minimum and maximum parameters values, because out-of-range values are often intentional and useful. If that isn't what you want, try pairing this function with :doc:`sketch_constrain`.

In Processing this functionality is provided by ``map()`` but was renamed in py5 because of a name conflict with a builtin Python function.

Signatures
----------

.. code:: python

    remap(
        value: Union[float, npt.NDArray],  # the incoming value to be converted
        start1: Union[float, npt.NDArray],  # lower bound of the value's current range
        stop1: Union[float, npt.NDArray],  # upper bound of the value's current range
        start2: Union[float, npt.NDArray],  # lower bound of the value's target range
        stop2: Union[float, npt.NDArray],  # upper bound of the value's target range
    ) -> Union[float, npt.NDArray]
Updated on September 01, 2022 12:53:02pm UTC

