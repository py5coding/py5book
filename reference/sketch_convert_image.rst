convert_image()
===============

Convert non-py5 image objects into Py5Image objects.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_convert_image_0.png
    :alt: example picture for convert_image()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    from PIL import Image


    def setup():
        pil_image = Image.open('data/apples.jpg')
        py5_image = py5.convert_image(pil_image)
        py5.image(py5_image, 0, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Convert non-py5 image objects into Py5Image objects. This facilitates py5 compatability with other commonly used Python libraries.

This method is comparable to :doc:`sketch_load_image`, except instead of reading image files from disk, it reads image data from other Python objects.

Passed image object types must be known to py5's image conversion tools. New object types and functions to effect conversions can be registered with :doc:`py5functions_register_image_conversion`.

The ``convert_image()`` method has builtin support for conversion of ``PIL.Image`` objects. This will allow users to use image formats that :doc:`sketch_load_image` cannot read. To convert a numpy array into a Py5Image, use :doc:`sketch_create_image_from_numpy`.

The caller can optionally pass an existing Py5Image object to put the converted image into using the ``dst`` parameter. This can have performance benefits in code that would otherwise continuously create new Py5Image objects. The converted image width and height must match that of the recycled Py5Image object.

Signatures
----------

.. code:: python

    convert_image(
        obj: Any,  # object to convert into a Py5Image object
        *,
        dst: Py5Image = None  # existing Py5Image object to put the converted image into
    ) -> Py5Image

Updated on September 01, 2022 14:08:27pm UTC

