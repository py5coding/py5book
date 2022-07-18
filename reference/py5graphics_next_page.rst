Py5Graphics.next_page()
=======================

Move to the next page in a PDF document.

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
        py5.size(600, 600, py5.PDF, "/tmp/test.pdf")


    def draw():
        for _ in range(50):
            py5.rect(py5.random_int(py5.width), py5.random_int(py5.height), 10, 10)

        if py5.frame_count < 5:
            py5.g.next_page()
        else:
            py5.exit_sketch()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Move to the next page in a PDF document. This method is only available when using a ``PDF`` :doc:`py5graphics` object. Using this method with any other graphics renderer will result in an error.

Underlying Processing method: PGraphics.nextPage

Syntax
------

.. code:: python

    next_page() -> None

Updated on July 18, 2022 17:37:19pm UTC

