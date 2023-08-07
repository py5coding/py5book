# py5_tools.screenshot()

Take a screenshot of a running Sketch.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import time
import py5_tools

py5.run_sketch()
# take a screenshot of the running sketch after a two second delay
time.sleep(2)
img = py5_tools.screenshot()
img.save('image.png')
```

</div></div>

</div>

## Description

Take a screenshot of a running Sketch.

The returned image is a `PIL.Image` object. It can be assigned to a variable or embedded in the notebook.

By default the Sketch will be the currently running Sketch, as returned by [](py5functions_get_current_sketch). Use the `sketch` parameter to specify a different running Sketch, such as a Sketch created using Class mode.

If your Sketch has a `post_draw()` method, use the `hook_post_draw` parameter to make this function run after `post_draw()` instead of `draw()`. This is important when using Processing libraries that support `post_draw()` such as Camera3D or ColorBlindness.

## Signatures

```python
screenshot(
    *,
    sketch: Sketch = None,  # running Sketch
    hook_post_draw: bool = False  # attach hook to Sketch's post_draw method instead of draw
) -> PIL_Image
```

Updated on August 07, 2023 14:29:21pm UTC
