select_input()
==============

Open a file chooser dialog to select a file for input.

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

    def file_selected(selection):
        if selection is None:
            py5.println("Window was closed or the user hit cancel.")
        else:
            py5.println("User selected " + selection)


    def setup():
        py5.select_input("Select a file to process:", file_selected)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Open a file chooser dialog to select a file for input. After the selection is made, the selected File will be passed to the ``callback`` function. If the dialog is closed or canceled, ``None`` will be sent to the function, so that the program is not waiting for additional input. The callback is necessary because of how threading works.

This method has some platform specific quirks. On OSX, this does not work when the Sketch is run through a Jupyter notebook. On Windows, Sketches using the OpenGL renderers (``P2D`` or ``P3D``) will be minimized while the select dialog box is open. This method only uses native dialog boxes on OSX.

Underlying Processing method: `selectInput <https://processing.org/reference/selectInput_.html>`_

Syntax
------

.. code:: python

    select_input(prompt: str, callback: Callable, default_file: str = None) -> None

Parameters
----------

* **callback**: `Callable` - callback function after selection is made
* **default_file**: `str = None` - default output file
* **prompt**: `str` - text prompt for select dialog box


Updated on July 31, 2022 19:10:43pm UTC

