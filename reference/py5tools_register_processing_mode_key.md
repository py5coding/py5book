# py5_tools.register_processing_mode_key()

Register a callable or module when programming in py5's Processing Mode.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import numpy as np

import py5_tools
import py5


def alter_image(msg: str, img: py5.Py5Image):
    py5.println("PYTHON:", msg)
    py5.println("PYTHON:", img)

    img.load_np_pixels()
    img.np_pixels[::2, ::2] = [255, 255, 0, 0]
    img.update_np_pixels()

    return img


py5_tools.register_processing_mode_key('test_transfer', alter_image)
py5_tools.register_processing_mode_key('np', np)

py5.run_sketch(jclassname='test.TestSketch')
```

</div></div>

</div>

## Description

Register a callable or module when programming in py5's Processing Mode. This will make Python code available to Processing Mode py5 users to call in Java with the `callPython()` method. Please read py5's online documentation to learn more about Processing Mode.

The `value` parameter can be a callable, a module or an object. If `value` is a module or an object, the `key` parameter in the Java `callPython()` call should use dots (`.`) to access the module's or object's callables.

## Signatures

```python
register_processing_mode_key(
    key: str,  # key used from Processing Mode callPython() method
    value: Union[Callable, ModuleType],  # callable or module to link to key
    *,
    callback_once: bool = False  # deregister key after single use
) -> None
```

Updated on April 15, 2023 22:56:12pm UTC
