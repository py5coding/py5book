request_image()
===============

Use a Py5Promise object to load an image into a variable of type ``Py5Image``.

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

    def draw():
        global img_promise
        if py5.frame_count == 1:
            # the request should only be made once
            img_promise = py5.request_image('http://py5.ixora.io/files/apples.jpg')

        py5.background(0)
        if img_promise.is_ready:
            py5.image(img_promise.result, 10, 10)
        else:
            py5.println('not ready')

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Use a Py5Promise object to load an image into a variable of type ``Py5Image``. This method provides a convenient alternative to combining :doc:`sketch_launch_promise_thread` with :doc:`sketch_load_image` to load image data.

Consider using ``request_image()`` to load image data from within a Sketch's ``draw()`` function. Using :doc:`sketch_load_image` in the ``draw()`` function would slow down the Sketch animation.

The returned Py5Promise object has an ``is_ready`` property that will be ``True`` when the ``result`` property contains the value function ``f`` returned. Before then, the ``result`` property will be ``None``.

Signatures
----------

.. code:: python

    request_image(
        image_path: Union[str, Path]  # url or file path for image file
    ) -> Py5Promise
Updated on September 01, 2022 12:53:02pm UTC

