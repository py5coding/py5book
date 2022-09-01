no_loop()
=========

Stops py5 from continuously executing the code within ``draw()``.

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
        py5.size(200, 200)
        py5.no_loop()


    def draw():
        py5.line(10, 10, 190, 190)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    x = 0.0


    def setup():
        py5.size(200, 200)


    def draw():
        global x
        py5.background(204)
        x = x + 0.1
        if x > py5.width:
            x = 0
        py5.line(x, 0, x, py5.height)


    def mouse_pressed():
        py5.no_loop()


    def mouse_released():
        py5.loop()

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    some_mode = False


    def setup():
        py5.no_loop()


    def draw():
        if some_mode:
            # do something
            pass


    def mouse_pressed():
        some_mode = True
        py5.redraw()  # or call loop()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Stops py5 from continuously executing the code within ``draw()``. If :doc:`sketch_loop` is called, the code in ``draw()`` begins to run continuously again. If using ``no_loop()`` in ``setup()``, it should be the last line inside the block.

When ``no_loop()`` is used, it's not possible to manipulate or access the screen inside event handling functions such as ``mouse_pressed()`` or ``key_pressed()``. Instead, use those functions to call :doc:`sketch_redraw` or :doc:`sketch_loop`, which will run ``draw()``, which can update the screen properly. This means that when ``no_loop()`` has been called, no drawing can happen, and functions like :doc:`sketch_save_frame` or :doc:`sketch_load_pixels` may not be used.

Note that if the Sketch is resized, :doc:`sketch_redraw` will be called to update the Sketch, even after ``no_loop()`` has been specified. Otherwise, the Sketch would enter an odd state until :doc:`sketch_loop` was called.

Underlying Processing method: `noLoop <https://processing.org/reference/noLoop_.html>`_

Signatures
----------

.. code:: python

    no_loop() -> None

Updated on September 01, 2022 14:08:27pm UTC

