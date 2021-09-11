radians()
=========

Converts a degree measurement to its corresponding value in radians.

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
        deg = 45
        rad = py5.radians(deg)
        # prints "45 degrees is 0.7854 radians"
        py5.println(round(deg, 5), 'degrees is', round(rad, 5), 'radians')

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Converts a degree measurement to its corresponding value in radians. Radians and degrees are two ways of measuring the same thing. There are 360 degrees in a circle and ``2*PI`` radians in a circle. For example, ``90° = PI/2 = 1.5707964``. All trigonometric functions in py5 require their parameters to be specified in radians.

This function makes a call to the numpy ``radians()`` function.

Syntax
------

.. code:: python

    radians(degrees: float) -> float

Parameters
----------

* **degrees**: `float` - degree value to convert to radians


Updated on September 11, 2021 16:51:34pm UTC

