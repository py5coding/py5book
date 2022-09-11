Py5Vector
=========

Class to describe a 2D, 3D, or 4D vector.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    import numpy as np

    v1 = py5.Py5Vector(1, 2, 3)
    print(v1)
    # Py5Vector3D(1., 2., 3.)

    v2 = py5.Py5Vector(dim=4)
    print(v2)
    # Py5Vector4D(0., 0., 0., 0.)

    v3 = py5.Py5Vector(1 / 3, 1 / 7, dtype=np.float16)
    print(v3)
    # Py5Vector2D(0.3333, 0.1428)

    v4 = py5.Py5Vector([1, 2, 3])
    print(v4)
    # Py5Vector3D(1., 2., 3.)

    v5 = py5.Py5Vector(v4, 0)
    print(v5)
    # Py5Vector4D(1., 2., 3., 0.)

    arr = np.array([1., 2., 3.])
    v6 = py5.Py5Vector(arr, copy=False)
    print(v6)
    # Py5Vector3D(1., 2., 3.)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Class to describe a 2D, 3D, or 4D vector. A vector is an entity that has both a magnitude and a direction. This datatype stores the components of the vector as a set of coordinates. A 3D vector, for example, has :doc:`py5vector_x`, :doc:`py5vector_y`, and :doc:`py5vector_z` values that quantify the vector along the 3 dimensions X, Y, and Z. The magnitude and direction can be accessed via the properties :doc:`py5vector_mag` and :doc:`py5vector_heading`.

In many of the py5 examples, you will see ``Py5Vector`` used to describe a position, velocity, or acceleration. For example, if you consider a rectangle moving across the screen, at any given instant it has a position (a vector that points from the origin to its location), a velocity (the rate at which the object's position changes per time unit, expressed as a vector), and acceleration (the rate at which the object's velocity changes per time unit, expressed as a vector).

The ``Py5Vector`` class works well with numpy and in most cases you will be able to do math operations that combine vectors and numpy arrays.

To create a vector, you can write code like ``v = Py5Vector(1, 2, 3)``, which would create a 3D vector with the x, y, and z values equal to 1, 2, and 3. To create a vector of zeros, omit the vector values and specify the desired dimension with the ``dim`` parameter, such as ``v = Py5Vector(dim=4)``.

Internally, Py5Vector stores the vector values in a numpy array. By default, the data type (dtype) of that numpy array is the default float size for your computer, which is typically a 64 bit float, or ``np.float64``. To create a vector with a different float size, pass your desired numpy float dtype to the ``dtype`` parameter, like ``v3 = py5.Py5Vector(1 / 3, 1 / 7, dtype=np.float16)``.

When creating a new Py5Vector, the initial vector values need not be discrete values. You can provide a list of numbers, a numpy array, or another Py5Vector. For example, ``v4 = py5.Py5Vector([1, 2, 3])`` creates a Py5Vector from a list, and ``v5 = py5.Py5Vector(v4, 0)`` creates a 4D Py5Vector from a 3D Py5Vector and a constant value.

When creating a new Py5Vector from a single numpy array, py5 will by default create its own copy of the numpy array for the Py5Vector to use. To instruct py5 to instead use the same numpy array and share its data with provided array, set the ``copy`` parameter to ``False``, such as ``v6 = py5.Py5Vector(arr, copy=False)``.

The following methods and fields are provided:

.. include:: include_py5vector.rst

Updated on September 01, 2022 16:36:02pm UTC

