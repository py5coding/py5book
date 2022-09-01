background()
============

The ``background()`` function sets the color used for the background of the py5 window.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_background_0.png
    :alt: example picture for background()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        py5.background(51)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_background_1.png
    :alt: example picture for background()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        py5.background(255, 204, 0)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_background_2.png
    :alt: example picture for background()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        img = py5.load_image("laDefense.jpg")
        py5.background(img)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

The ``background()`` function sets the color used for the background of the py5 window. The default background is light gray. This function is typically used within ``draw()`` to clear the display window at the beginning of each frame, but it can be used inside ``setup()`` to set the background on the first frame of animation or if the backgound need only be set once.
 
An image can also be used as the background for a Sketch, although the image's width and height must match that of the Sketch window. Images used with ``background()`` will ignore the current :doc:`sketch_tint` setting. To resize an image to the size of the Sketch window, use ``image.resize(width, height)``.
 
It is not possible to use the transparency ``alpha`` parameter with background colors on the main drawing surface. It can only be used along with a ``Py5Graphics`` object and :doc:`sketch_create_graphics`.

Underlying Processing method: `background <https://processing.org/reference/background_.html>`_

Signatures
----------

.. code:: python

    background(
        gray: float,  # specifies a value between white and black
        /,
    ) -> None

    background(
        gray: float,  # specifies a value between white and black
        alpha: float,  # opacity of the background
        /,
    ) -> None

    background(
        image: Py5Image,  # Py5Image to set as background (must be same size as the Sketch window)
        /,
    ) -> None

    background(
        rgb: int,  # any value of the color datatype
        /,
    ) -> None

    background(
        rgb: int,  # any value of the color datatype
        alpha: float,  # opacity of the background
        /,
    ) -> None

    background(
        v1: float,  # red or hue value (depending on the current color mode)
        v2: float,  # green or saturation value (depending on the current color mode)
        v3: float,  # blue or brightness value (depending on the current color mode)
        /,
    ) -> None

    background(
        v1: float,  # red or hue value (depending on the current color mode)
        v2: float,  # green or saturation value (depending on the current color mode)
        v3: float,  # blue or brightness value (depending on the current color mode)
        alpha: float,  # opacity of the background
        /,
    ) -> None

Updated on September 01, 2022 16:36:02pm UTC

