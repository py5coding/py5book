floor()
=======

Calculates the closest int value that is less than or equal to the value of the parameter.

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
        x = 2.88
        a = py5.floor(x)  # Sets 'a' to 2

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Calculates the closest int value that is less than or equal to the value of the parameter.

This function makes a call to the numpy ``floor()`` function.

Syntax
------

.. code:: python

    floor(value: float) -> int

Parameters
----------

* **value**: `float` - number to round down


Updated on September 11, 2021 16:51:34pm UTC

