ceil()
======

Calculates the closest int value that is greater than or equal to the value of the parameter.

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
        a = py5.ceil(x)  # Sets 'a' to 3

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Calculates the closest int value that is greater than or equal to the value of the parameter.

This function makes a call to the numpy ``ceil()`` function.

Signatures
------

.. code:: python

    ceil(
        value: Union[float, npt.ArrayLike]  # number to round up
    ) -> Union[int, npt.NDArray]
Updated on August 25, 2022 20:01:47pm UTC

