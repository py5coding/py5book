year()
======

Py5 communicates with the clock on your computer.

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
        d = py5.day()    # values from_ 1 - 31
        m = py5.month()  # values from_ 1 - 12
        y = py5.year()   # 2003, 2004, 2005, etc.
    
        py5.text(str(d), 10, 28)
        py5.text(str(m), 10, 56)
        py5.text(str(y), 10, 84)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Py5 communicates with the clock on your computer. The ``year()`` function returns the current year as an integer (2003, 2004, 2005, etc).

Underlying Processing method: `year <https://processing.org/reference/year_.html>`_

Signatures
----------

.. code:: python

    year() -> int

Updated on September 01, 2022 14:08:27pm UTC

