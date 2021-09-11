end_raw()
=========

Complement to :doc:`sketch_begin_raw`; they must always be used together.

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
        py5.size(400, 400, py5.P2D)
        py5.begin_raw(py5.PDF, "raw.pdf")


    def draw():
        py5.line(py5.pmouse_x, py5.pmouse_y, py5.mouse_x, py5.mouse_y)


    def key_pressed():
        if py5.key == ' ':
            py5.end_raw()
            py5.exit_sketch()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Complement to :doc:`sketch_begin_raw`; they must always be used together. See the :doc:`sketch_begin_raw` reference for details.

Underlying Java method: `endRaw <https://processing.org/reference/endRaw_.html>`_

Syntax
------

.. code:: python

    end_raw() -> None

Updated on September 11, 2021 16:51:34pm UTC

