# py5_tools.sketch_portal()

Creates a portal widget to continuously stream frames from a running Sketch into a Jupyter notebook.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import py5_tools

py5.run_sketch(block=False)
# stream frames from the currently running sketch for 5 seconds
portal = py5_tools.sketch_portal(time_limit=5)

portal
```

</div></div>

</div>

## Description

Creates a portal widget to continuously stream frames from a running Sketch into a Jupyter notebook. Each frame will appear embedded in the notebook, with each new frame replacing the previous frame.

**Unfortunately, the Sketch Portal feature had to be removed from py5 in release 0.10.0. Changes to Jupyter Lab and Jupyter Widgets somehow broke the code and it was too difficult to figure out why. Rather than fix the code, the Sketch Portal will be re-implemented using the Python library anywidget. This new approach will hopefully be simpler to implement and easier to maintain.**

By default the Sketch will be the currently running Sketch, as returned by [](py5functions_get_current_sketch). Use the `sketch` parameter to specify a different running Sketch, such as a Sketch created using [class mode](content-py5-modes-class-mode).

The Sketch Portal is a custom Jupyter Widget and can handle keyboard or mouse events just like a native window. You will need to click on the portal for it to gain focus and capture keyboard events. Mouse and keyboard events will be observed by the browser and simulated events will be created for the Sketch. Every effort has been made to make the simulated events identical to real events but some small differences remain. You can also use the Jupyter-provided Widgets such as sliders and text boxes for user input.

This function is intended to be used when a real display is not available, such as when using py5 through an online Jupyter notebook system like binder (mybinder.org). You are free to execute code elsewhere in the notebook while the Sketch is running and the portal is open. This function can only be used in a Jupyter Notebook. It uses ZMQ to stream JPEG images from the kernel to the client front-end.

If you are using Jupyter Lab, try right clicking in the output area of the cell and selecting "Create New View for Output". This will create a new panel just for the Sketch Portal. Creating a "New Console for Notebook" and creating a portal there works well also.

This command can be called before [](sketch_run_sketch) if the current Sketch is in the [](sketch_is_ready) state.

Use the `time_limit` parameter to set a time limit (seconds). Use `throttle_frame_rate` to throttle the stream's frame rate (frames per second) to a slower pace than the Sketch's actual draw frame rate. By default, `throttle_frame_rate` is set to 30, which is half of the Sketch's default draw frame rate of 60 frames per second. Set this parameter to `None` to disable throttling. The `scale` parameter is a scaling factor that can adjust the portal height and width. The `quality` parameter sets the JPEG quality factor (default 75) for the stream, which must be between 1 (worst) and 100 (best). If the portal causes the Sketch's frame rate to drop, try adjusting the portal's throttle frame rate, quality, and scale.

If your Sketch has a `post_draw()` method, use the `hook_post_draw` parameter to make this function run after `post_draw()` instead of `draw()`. This is important when using Processing libraries that support `post_draw()` such as Camera3D or ColorBlindness.

To stop a Sketch Portal, wait for the time limit to expire, call [](sketch_exit_sketch), or press the "exit_sketch()" button below the portal. If you delete the cell with the `Py5SketchPortal` object, the portal will no longer be visible but the Sketch will still be streaming frames to the notebook client, wasting resources. A Sketch can only have one open portal, so opening a new portal with different options will replace an existing portal.

## Signatures

```python
sketch_portal(
    *,
    time_limit: float = 0.0,  # time limit in seconds for the Sketch Portal; set to 0 (default) for no limit
    throttle_frame_rate: float = 30,  # throttle portal frame rate below Sketch's frame rate
    scale: float = 1.0,  # scale factor to adjust the height and width of the portal
    quality: int = 75,  # JPEG stream quality between 1 (worst) and 100 (best)
    portal_widget: Py5SketchPortal = None,  # Py5SketchPortal object to send stream to
    sketch: Sketch = None,  # running Sketch
    hook_post_draw: bool = False  # attach hook to Sketch's post_draw method instead of draw
) -> None
```

Updated on March 18, 2024 05:08:14am UTC
