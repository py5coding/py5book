norm()
======

Normalizes a number from another range into a value between 0 and 1.

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
        value = 20
        n = py5.norm(value, 0, 50)
        py5.println(n)  # Prints "0.4"

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        value = -10
        n = py5.norm(value, 0, 100)
        py5.println(n)  # Prints "-0.1"

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Normalizes a number from another range into a value between 0 and 1. Identical to ``remap(value, low, high, 0, 1)``.

Numbers outside of the range are not clamped to 0 and 1, because out-of-range values are often intentional and useful. (See the second example.) If that isn't what you want, try pairing this function with :doc:`sketch_constrain`.

Syntax
------

.. code:: python

    norm(value: Union[float, npt.NDArray], start: Union[float, npt.NDArray], stop: Union[float, npt.NDArray]) -> Union[float, npt.NDArray]

Parameters
----------

* **start**: `Union[float, npt.NDArray]` - lower bound of the value's current range
* **stop**: `Union[float, npt.NDArray]` - upper bound of the value's current range
* **value**: `Union[float, npt.NDArray]` - the incoming value to be converted


Updated on February 26, 2022 13:22:44pm UTC

