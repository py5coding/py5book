window_title()
==============

Set the Sketch window's title.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        py5.size(200, 200)
        py5.window_title("py5 window")

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Set the Sketch window's title. This will typically appear at the window's title bar. The default window title is "Sketch".

This method provides the same functionality as :doc:`py5surface_set_title` but without the need to interact directly with the :doc:`py5surface` object.

Underlying Processing method: windowTitle

Signatures
----------

.. code:: python

    window_title(
        title: str,  # new window title
        /,
    ) -> None

Updated on September 01, 2022 16:36:02pm UTC

