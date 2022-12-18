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

Signatures
----------

.. code:: python

    constrain(
        amt: Union[float, npt.NDArray],  # the value to constrain
        low: Union[float, npt.NDArray],  # maximum limit
        high: Union[float, npt.NDArray],  # minimum limit
    ) -> Union[float, npt.NDArray]

Updated on September 01, 2022 16:36:02pm UTC

