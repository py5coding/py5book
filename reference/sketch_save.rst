save()
======

Save the drawing surface to an image file.

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
        for _ in range(10):
            py5.rect(py5.random_int(py5.width), py5.random_int(py5.height), 10, 10)
        py5.save('/tmp/random_squares.jpg')

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Save the drawing surface to an image file. This method uses the Python library Pillow to write the image, so it can save images in any format that that library supports.

Use the ``drop_alpha`` parameter to drop the alpha channel from the image. This defaults to ``True``. Some image formats such as JPG do not support alpha channels, and Pillow will throw an error if you try to save an image with the alpha channel in that format.

The ``use_thread`` parameter will save the image in a separate Python thread. This improves performance by returning before the image has actually been written to the file.

Signatures
------

.. code:: python

    save(
        filename: Union[str, Path, BytesIO],  # output filename
        *,
        format: str = None,  # image format, if not determined from filename extension
        drop_alpha: bool = True,  # remove the alpha channel when saving the image
        use_thread: bool = False,  # write file in separate thread
        **params
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

