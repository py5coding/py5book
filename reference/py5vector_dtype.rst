Py5Vector.dtype
===============

Vector data type.

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

    import numpy as np

    v1 = py5.Py5Vector(1, 2, 3)
    v2 = v1.astype(np.float16)

    print(repr(v1.dtype))
    # dtype('float64')
    print(repr(v2.dtype))
    # dtype('float16')

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Vector data type. This will be one of ``np.float16``, ``np.float32``, ``np.float64``, or ``np.float128``.

Updated on August 25, 2022 20:01:47pm UTC

