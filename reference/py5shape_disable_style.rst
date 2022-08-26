Py5Shape.disable_style()
========================

Disables the shape's style data and uses py5's current styles.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_disable_style_0.png
    :alt: example picture for disable_style()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global s
        # the file "bot.svg" must be in the data folder
        # of the current sketch to load successfully
        s = py5.load_shape("bot.svg")


    def draw():
        s.disable_style()
        py5.shape(s, -30, 10, 80, 80)
        s.enable_style()
        py5.shape(s, 50, 10, 80, 80)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Disables the shape's style data and uses py5's current styles. Styles include attributes such as colors, stroke weight, and stroke joints.

Underlying Processing method: `PShape.disableStyle <https://processing.org/reference/PShape_disableStyle_.html>`_

Signatures
------

.. code:: python

    disable_style() -> None
Updated on August 25, 2022 20:01:47pm UTC

