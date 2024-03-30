# py5_tools.animated_gif()

Create an animated GIF using a running Sketch.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import py5_tools

py5.run_sketch(block=False)
# create a 10 frame animated GIF saved to '/tmp/animated.gif'
py5_tools.animated_gif('/tmp/animated.gif', count=10, period=1, duration=0.5)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import py5_tools

# make an animated GIF with specific frames, save to '/tmp/animated.gif'
py5_tools.animated_gif('/tmp/animated.gif', frame_numbers=[0, 1, 3, 5, 13], duration=0.5)

py5.run_sketch()
```

</div></div>

</div>

## Description

Create an animated GIF using a running Sketch.

You have two choices for how to specify which frames should be included in the animated GIF. The first choice is to use the `count` keyword argument to include a specific number of frames. Optionally, the `period` keyword argument can also be used with `count` to introduce a fixed time delay between captured frames. The second choice is to use the `frame_numbers` keyword argument to pass a list of frame numbers. A frame will be included when the [](sketch_frame_count) value is in the list passed to `frame_numbers`. For this feature, frame number 0 is after `setup()` is complete and frame number 1 is after the first call to `draw()`.

Bottom line, you must use either the `count` parameter or the `frame_numbers` parameter but not both. The `period` parameter can only be used in conjunction with the `count` parameter. The duration parameter must always be used.

By default this function will return right away and construct the animated gif in the background while the Sketch is running. The completed gif will be saved to the location specified by the `filename` parameter when it is ready. Set the `block` parameter to `True` to instruct the function to not return until the gif construction is complete. This blocking feature is not available on macOS when the Sketch is executed through an IPython kernel. If the Sketch terminates prematurely, no gif will be created.

By default the Sketch will be the currently running Sketch, as returned by [](py5functions_get_current_sketch). Use the `sketch` parameter to specify a different running Sketch, such as a Sketch created using [class mode](content-py5-modes-class-mode).

If your Sketch has a `post_draw()` method, use the `hook_post_draw` parameter to make this function run after `post_draw()` instead of `draw()`. This is important when using Processing libraries that support `post_draw()` such as Camera3D or ColorBlindness.

## Signatures

```python
animated_gif(
    filename: str,  # filename of GIF to create
    *,
    count: int = 0,  # number of Sketch snapshots to create
    period: float = 0.0,  # time in seconds between Sketch snapshots
    frame_numbers: Iterable = None,  # list of frame numbers to include in animated GIF
    duration: float = 0.0,  # time in seconds between frames in the GIF
    loop: int = 0,  # number of times for the GIF to loop (default of 0 loops indefinitely)
    optimize: bool = True,  # optimize GIF palette
    sketch: Sketch = None,  # running Sketch
    hook_post_draw: bool = False,  # attach hook to Sketch's post_draw method instead of draw
    block: bool = False  # function returns immediately (False) or blocks until function returns (True)
) -> None
```

Updated on March 18, 2024 05:08:14am UTC
