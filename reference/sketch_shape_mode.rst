shape_mode()
============

Modifies the location from which shapes draw.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_shape_mode_0.png
    :alt: example picture for shape_mode()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        global bot
        bot = py5.load_shape("bot.svg")


    def draw():
        py5.shape_mode(py5.CENTER)
        py5.shape(bot, 35, 35, 50, 50)
        py5.shape_mode(py5.CORNER)
        py5.shape(bot, 35, 35, 50, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Modifies the location from which shapes draw. The default mode is ``shape_mode(CORNER)``, which specifies the location to be the upper left corner of the shape and uses the third and fourth parameters of :doc:`sketch_shape` to specify the width and height. The syntax ``shape_mode(CORNERS)`` uses the first and second parameters of :doc:`sketch_shape` to set the location of one corner and uses the third and fourth parameters to set the opposite corner. The syntax ``shape_mode(CENTER)`` draws the shape from its center point and uses the third and forth parameters of :doc:`sketch_shape` to specify the width and height. The parameter must be written in ALL CAPS because Python is a case sensitive language.

Underlying Processing method: `shapeMode <https://processing.org/reference/shapeMode_.html>`_

Signatures
----------

.. code:: python

    shape_mode(
        mode: int,  # either CORNER, CORNERS, CENTER
        /,
    ) -> None

Updated on September 01, 2022 16:36:02pm UTC

