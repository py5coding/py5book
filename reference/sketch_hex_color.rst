hex_color()
===========

Convert a color value to a hex color string.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_hex_color_0.png
    :alt: example picture for hex_color()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        c = py5.color(15, 63, 240)
        hex_c = py5.hex_color(c)
        py5.text_size(20)
        py5.fill(hex_c)
        py5.text(hex_c, 5, 55)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Convert a color value to a hex color string. Processing and py5 store color values in 32 bit integers that are inconvenient for a human to parse. To interpret these values, one can use methods like :doc:`sketch_red`, :doc:`sketch_green`, and :doc:`sketch_blue` to extract color channel values from the 32 bit integers. This method provides an alternative approach, converting the 32 bit integer into a string such as ``'#0F3FF0FF'``. The hex string has 8 hexadecimal values following a ``#`` character. The first two values represent the red value, the next two green, the next two blue, and the last two alpha. This is similar to web colors except for the addition of the alpha channel.

Conveniently, the hex color string returned by this method can also be used as parameter for other methods that accept color values. Observe how this is done in the example code.

Syntax
------

.. code:: python

    hex_color(color: int) -> str

Parameters
----------

* **color**: `int` - any color value


Updated on July 31, 2022 13:33:17pm UTC

