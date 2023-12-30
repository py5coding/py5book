# convert_image()

Convert non-py5 image objects into Py5Image objects.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for convert_image()](/images/reference/Sketch_convert_image_0.png)

</div><div class="example-cell-code">

```python
from PIL import Image


def setup():
    pil_image = Image.open('data/apples.jpg')
    py5_image = py5.convert_image(pil_image)
    py5.image(py5_image, 0, 0)
```

</div></div>

</div>

## Description

Convert non-py5 image objects into Py5Image objects. This facilitates py5 compatability with other commonly used Python libraries.

This method is comparable to [](sketch_load_image), except instead of reading image files from disk, it converts image data from other Python objects.

Passed image object types must be known to py5's image conversion tools. New object types and functions to effect conversions can be registered with [](py5functions_register_image_conversion).

The `convert_image()` method has builtin support for the conversion of `PIL.Image` objects. This will allow users to use image formats that [](sketch_load_image) cannot read. Look at the online ["Images and Pillow"](/integrations/pillow) Python Ecosystem Integration tutorial for more information. To convert a numpy array into a Py5Image, use [](sketch_create_image_from_numpy).

The caller can optionally pass an existing Py5Image object to put the converted image into using the `dst` parameter. This can have performance benefits in code that would otherwise continuously create new Py5Image objects. The converted image width and height must match that of the recycled Py5Image object.

The `convert_image()` method has builtin support for the conversion of matplotlib charts and Cairo surfaces. Look at the online ["Charts, Plots, and Matplotlib"](/integrations/matplotlib) and ["SVG Images and Cairo"](/integrations/cairo) Python Ecosystem Integration tutorials for more information. You can also create your own custom integrations. Look at the online ["Custom Integrations"](/integrations/custom_integrations) Python Ecosystem Integration tutorial to learn more.

## Signatures

```python
convert_image(
    obj: Any,  # object to convert into a Py5Image object
    *,
    dst: Py5Image = None,  # existing Py5Image object to put the converted image into
    **kwargs: dict[str, Any]
) -> Py5Image
```

Updated on December 26, 2023 12:27:15pm UTC
