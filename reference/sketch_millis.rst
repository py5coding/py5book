millis()
========

Returns the number of milliseconds (thousandths of a second) since starting the program.

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
        m = py5.millis()
        py5.no_stroke()
        py5.fill(m%255)
        py5.rect(25, 25, 50, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Returns the number of milliseconds (thousandths of a second) since starting the program. This information is often used for timing events and animation sequences.

Underlying Processing method: `millis <https://processing.org/reference/millis_.html>`_

Signatures
------

.. code:: python

    millis() -> int
Updated on August 25, 2022 20:01:47pm UTC

