degrees()
=========

Converts a radian measurement to its corresponding value in degrees.

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

    def setup():
        rad = py5.PI/4
        deg = py5.degrees(rad)
        # prints "0.7854 radians is 45.0 degrees"
        py5.println(round(rad, 5), 'radians is', round(deg, 5), 'degrees')

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Converts a radian measurement to its corresponding value in degrees. Radians and degrees are two ways of measuring the same thing. There are 360 degrees in a circle and ``2*PI`` radians in a circle. For example, ``90° = PI/2 = 1.5707964``. All trigonometric functions in py5 require their parameters to be specified in radians.

This function makes a call to the numpy ``degrees()`` function.

Syntax
------

.. code:: python

    degrees(radians: Union[float, npt.ArrayLike]) -> Union[float, npt.NDArray]

Parameters
----------

* **radians**: `Union[float, npt.ArrayLike]` - radian value to convert to degrees


Updated on February 26, 2022 13:22:44pm UTC

