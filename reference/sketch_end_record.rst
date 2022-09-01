end_record()
============

Stops the recording process started by :doc:`sketch_begin_record` and closes the file.

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
        py5.size(400, 400)
        py5.begin_record(py5.PDF, "everything.pdf")


    def draw():
        py5.ellipse(py5.mouse_x, py5.mouse_y, 10, 10)


    def mouse_pressed():
        py5.end_record()
        py5.exit_sketch()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Stops the recording process started by :doc:`sketch_begin_record` and closes the file.

Underlying Processing method: `endRecord <https://processing.org/reference/endRecord_.html>`_

Signatures
----------

.. code:: python

    end_record() -> None
Updated on September 01, 2022 12:53:02pm UTC

