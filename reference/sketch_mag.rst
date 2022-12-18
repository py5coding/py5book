mag()
=====

Calculates the magnitude (or length) of a vector.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_mag_0.png
    :alt: example picture for mag()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        x1 = 20
        x2 = 80
        y1 = 30
        y2 = 70

        py5.line(0, 0, x1, y1)
        py5.println(py5.mag(x1, y1))  # Prints "36.05551"
        py5.line(0, 0, x2, y1)
        py5.println(py5.mag(x2, y1))  # Prints "85.44004"
        py5.line(0, 0, x1, y2)
        py5.println(py5.mag(x1, y2))  # Prints "72.8011"
        py5.line(0, 0, x2, y2)
        py5.println(py5.mag(x2, y2))  # Prints "106.30146"

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Calculates the magnitude (or length) of a vector. A vector is a direction in space commonly used in computer graphics and linear algebra. Because it has no "start" position, the magnitude of a vector can be thought of as the distance from the coordinate ``(0, 0)`` to its ``(x, y)`` value. Therefore, ``mag()`` is a shortcut for writing ``dist(0, 0, x, y)``.

Signatures
----------

.. code:: python

    mag(
        a: Union[float, npt.NDArray],  # first value
        b: Union[float, npt.NDArray],  # second value
        /,
    ) -> float

    mag(
        a: Union[float, npt.NDArray],  # first value
        b: Union[float, npt.NDArray],  # second value
        c: Union[float, npt.NDArray],  # third value
        /,
    ) -> float

Updated on September 01, 2022 16:36:02pm UTC

