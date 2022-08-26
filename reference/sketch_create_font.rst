create_font()
=============

Dynamically converts a font to the format used by py5 from a .ttf or .otf file inside the Sketch's "data" folder or a font that's installed elsewhere on the computer.

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
        global my_font
        py5.size(200, 200)
        # uncomment the following two lines to see the available fonts
        # string[] font_list = py5.Py5Font.list()
        # print_array(font_list)
        my_font = py5.create_font("DejaVu Sans", 32)
        py5.text_font(my_font)
        py5.text_align(py5.CENTER, py5.CENTER)
        py5.text("!@#$%", py5.width//2, py5.height//2)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Dynamically converts a font to the format used by py5 from a .ttf or .otf file inside the Sketch's "data" folder or a font that's installed elsewhere on the computer. If you want to use a font installed on your computer, use the ``Py5Font.list()`` method to first determine the names for the fonts recognized by the computer and are compatible with this function. Not all fonts can be used and some might work with one operating system and not others. When sharing a Sketch with other people or posting it on the web, you may need to include a .ttf or .otf version of your font in the data directory of the Sketch because other people might not have the font installed on their computer. Only fonts that can legally be distributed should be included with a Sketch.

The ``size`` parameter states the font size you want to generate. The ``smooth`` parameter specifies if the font should be antialiased or not. The ``charset`` parameter is an array of chars that specifies the characters to generate.

This function allows py5 to work with the font natively in the default renderer, so the letters are defined by vector geometry and are rendered quickly. In the ``P2D`` and ``P3D`` renderers, the function sets the project to render the font as a series of small textures. For instance, when using the default renderer, the actual native version of the font will be employed by the Sketch, improving drawing quality and performance. With the ``P2D`` and ``P3D`` renderers, the bitmapped version will be used to improve speed and appearance, but the results are poor when exporting if the Sketch does not include the .otf or .ttf file, and the requested font is not available on the machine running the Sketch.

Underlying Processing method: `createFont <https://processing.org/reference/createFont_.html>`_

Signatures
------

.. code:: python

    create_font(
        name: str,  # name of the font to load
        size: float,  # point size of the font
        /,
    ) -> Py5Font

    create_font(
        name: str,  # name of the font to load
        size: float,  # point size of the font
        smooth: bool,  # true for an antialiased font, false for aliased
        /,
    ) -> Py5Font

    create_font(
        name: str,  # name of the font to load
        size: float,  # point size of the font
        smooth: bool,  # true for an antialiased font, false for aliased
        charset: list[chr],  # array containing characters to be generated
        /,
    ) -> Py5Font
Updated on August 25, 2022 20:01:47pm UTC

