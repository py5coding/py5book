constrain()
===========

Constrains a value to not exceed a maximum and minimum value.

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
        py5.background(204)
        mx = py5.constrain(py5.mouse_x, 30, 70)
        py5.rect(mx-10, 40, 20, 20)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Constrains a value to not exceed a maximum and minimum value.

Syntax
------

.. code:: python

    constrain(amt: Union[float, npt.NDArray], low: Union[float, npt.NDArray], high: Union[float, npt.NDArray]) -> Union[float, npt.NDArray]

Parameters
----------

* **amt**: `Union[float, npt.NDArray]` - the value to constrain
* **high**: `Union[float, npt.NDArray]` - minimum limit
* **low**: `Union[float, npt.NDArray]` - maximum limit


Updated on February 26, 2022 13:22:44pm UTC

