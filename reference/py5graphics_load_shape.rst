Py5Graphics.load_shape()
========================

Loads geometry into a variable of type ``Py5Shape``.

Description
-----------

Loads geometry into a variable of type ``Py5Shape``. SVG and OBJ files may be loaded. To load correctly, the file must be located in the data directory of the current Sketch. In most cases, ``load_shape()`` should be used inside ``setup()`` because loading shapes inside ``draw()`` will reduce the speed of a Sketch.

Alternatively, the file maybe be loaded from anywhere on the local computer using an absolute path (something that starts with / on Unix and Linux, or a drive letter on Windows), or the filename parameter can be a URL for a file found on a network.

If the file is not available or an error occurs, ``None`` will be returned and an error message will be printed to the console. The error message does not halt the program, however the ``None`` value may cause errors if your code does not check whether the value returned is ``None``.

This method is the same as :doc:`sketch_load_shape` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_load_shape`.

Underlying Processing method: PGraphics.loadShape

Signatures
------

.. code:: python

    load_shape(
        filename: str,  # name of file to load, can be .svg or .obj
        /,
    ) -> Py5Shape

    load_shape(
        filename: str,  # name of file to load, can be .svg or .obj
        options: str,  # unused parameter
        /,
    ) -> Py5Shape
Updated on August 25, 2022 20:01:47pm UTC

