rect_mode()
===========

Modifies the location from which rectangles are drawn by changing the way in which parameters given to :doc:`sketch_rect` are intepreted.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_rect_mode_0.png
    :alt: example picture for rect_mode()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        py5.rect_mode(py5.CORNER)  # default rect_mode is CORNER
        py5.fill(255)  # set fill to white
        py5.rect(25, 25, 50, 50)  # draw white rect using CORNER mode
    
        py5.rect_mode(py5.CORNERS)  # set rect_mode to CORNERS
        py5.fill(100)  # set fill to gray
        py5.rect(25, 25, 50, 50)  # draw gray rect using CORNERS mode

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_rect_mode_1.png
    :alt: example picture for rect_mode()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        py5.rect_mode(py5.RADIUS)  # set rect_mode to RADIUS
        py5.fill(255)  # set fill to white
        py5.rect(50, 50, 30, 30)  # draw white rect using RADIUS mode
    
        py5.rect_mode(py5.CENTER)  # set rect_mode to CENTER
        py5.fill(100)  # set fill to gray
        py5.rect(50, 50, 30, 30)  # draw gray rect using CENTER mode

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Modifies the location from which rectangles are drawn by changing the way in which parameters given to :doc:`sketch_rect` are intepreted.

The default mode is ``rect_mode(CORNER)``, which interprets the first two parameters of :doc:`sketch_rect` as the upper-left corner of the shape, while the third and fourth parameters are its width and height.

``rect_mode(CORNERS)`` interprets the first two parameters of :doc:`sketch_rect` as the location of one corner, and the third and fourth parameters as the location of the opposite corner.

``rect_mode(CENTER)`` interprets the first two parameters of :doc:`sketch_rect` as the shape's center point, while the third and fourth parameters are its width and height.

``rect_mode(RADIUS)`` also uses the first two parameters of :doc:`sketch_rect` as the shape's center point, but uses the third and fourth parameters to specify half of the shapes's width and height.

The parameter must be written in ALL CAPS because Python is a case-sensitive language.

Underlying Processing method: `rectMode <https://processing.org/reference/rectMode_.html>`_

Signatures
----------

.. code:: python

    rect_mode(
        mode: int,  # either CORNER, CORNERS, CENTER, or RADIUS
        /,
    ) -> None

Updated on September 01, 2022 16:36:02pm UTC

