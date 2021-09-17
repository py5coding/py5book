Py5 Functions
=============

The py5 Functions are extra utility functions that make py5 easier to use.

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

    py5.create_font_file('Comic Sans', 20)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    sketch = py5.get_current_sketch()
    assert sketch.is_ready
    py5.run_sketch(block=False)
    assert sketch.is_running
    py5.exit_sketch()
    assert sketch.is_dead

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    @py5.render(400, 200)
    def draw_message(s: py5.Sketch):
        s.background(255)
        s.fill(255, 0, 0)
        s.text_size(20)
        s.text_align(s.CENTER, s.CENTER)
        s.text('hello world', s.width/2, s.height/2)

    frame = draw_message()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

The py5 Functions are extra utility functions that make py5 easier to use. For example, you can use these to Processing's vlw font files without having to use Processing's IDE.

The following functions are provided:

.. include:: include_py5functions.rst

Updated on September 16, 2021 14:31:43pm UTC

