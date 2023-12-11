# register_image_conversion()

Register new image conversion functionality to be used by [](sketch_convert_image).

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for register_image_conversion()](/images/reference/Py5Functions_register_image_conversion_0.png)

</div><div class="example-cell-code">

```python
import numpy as np
from PIL import Image

def pillow_image_to_ndarray_precondition(obj):
    return isinstance(obj, Image.Image)

# convert rotated PIL Images to NumpyImageArray objects
# (py5 will convert a NumpyImageArray object to a Py5Image object)
def pillow_image_to_ndarray_converter(img, **kwargs):
    rotate = kwargs.get('rotate', 180)
    if img.mode not in ["RGB", "RGBA"]:
        img = img.convert(mode="RGB")
    img = img.rotate(rotate)
    return py5.NumpyImageArray(np.asarray(img), img.mode)

py5.register_image_conversion(
    pillow_image_to_ndarray_precondition, pillow_image_to_ndarray_converter
)

def setup():
    pil_img = Image.open('data/rockies.jpg').reduce(2)
    img1 = py5.convert_image(pil_img)
    img2 = py5.convert_image(pil_img, rotate=45)
    py5.image(img1, 0, 25)
    py5.image(img2, 50, 25)
```

</div></div>

</div>

## Description

Register new image conversion functionality to be used by [](sketch_convert_image).  This will allow users to extend py5's capabilities and compatability within the Python ecosystem.

The `precondition` parameter must be a function that accepts an object as a parameter and returns `True` if and only if the `convert_function` can successfully convert the object.

The `convert_function` parameter must be a function that accepts an object as a parameter and returns either a filename that can be read by [](sketch_load_image), a `py5.NumpyImageArray` object, or a [](py5image) object. View py5's source code for detailed information about `py5.NumpyImageArray` objects. The `convert_function` will take care of loading an image from a returned image filename or converting the `py5.NumpyImageArray` object into a Py5Image object.

## Signatures

```python
register_image_conversion(
    precondition: Callable,  # predicate determining if an object can be converted
    convert_function: Callable,  # function to convert object to relevant image data
) -> None
```

Updated on December 11, 2023 16:58:45pm UTC
