random_seed()
=============

Sets the seed value for py5's random functions.

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
        py5.random_seed(42)
        a = py5.random()
        py5.random_seed(42)
        b = py5.random()
        # the values a and b will be the same
        py5.println(a, b)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.random_seed(0)
        for i in range(100):
            r = py5.random(255)
            py5.stroke(r)
            py5.line(i, 0, i, 100)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets the seed value for py5's random functions. This includes :doc:`sketch_random`, :doc:`sketch_random_int`, :doc:`sketch_random_choice`, and :doc:`sketch_random_gaussian`. By default, all of these functions would produce different results each time a program is run. Set the seed parameter to a constant value to return the same pseudo-random numbers each time the software is run.

Signatures
----------

.. code:: python

    random_seed(
        seed: int,  # seed value
    ) -> None
Updated on September 01, 2022 12:53:02pm UTC

