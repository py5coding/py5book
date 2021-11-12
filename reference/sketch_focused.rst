focused
=======

Confirms if a py5 program is "focused," meaning that it is active and will accept mouse or keyboard input.

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
        if py5.focused:
            py5.ellipse(25, 25, 50, 50)
        else:
            py5.line(0, 0, 100, 100)
            py5.line(100, 0, 0, 100)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Confirms if a py5 program is "focused," meaning that it is active and will accept mouse or keyboard input. This variable is ``True`` if it is focused and ``False`` if not.

Underlying Processing field: `focused <https://processing.org/reference/focused.html>`_


Updated on November 12, 2021 11:30:58am UTC

