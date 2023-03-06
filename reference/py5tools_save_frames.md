# py5_tools.save_frames()

Save a running Sketch's frames to a directory.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import py5_tools

py5.run_sketch()
# save the next 50 frames to the `/tmp/frames` directory
frames = py5_tools.save_frames('/tmp/frames', limit=50, start=0)
```

</div></div>

</div>

## Description

Save a running Sketch's frames to a directory.

By default this function will return right away and save frames in the background while the Sketch is running. The frames will be saved in the directory specified by the `dirname` parameter. Set the `block` parameter to `True` to instruct the method to not return until the number of frames saved reaches the number specified by the `limit` parameter. This blocking feature is not available on OSX when the Sketch is executed through an IPython kernel.

By default the Sketch will be the currently running Sketch, as returned by [](py5functions_get_current_sketch). Use the `sketch` parameter to specify a different running Sketch, such as a Sketch created using Class mode.

If the `limit` parameter is used, this function will wait to return a list of the filenames. If not, it will return right away as the frames are saved in the background. It will keep doing so as long as the Sketch continues to run.

If your Sketch has a `post_draw()` method, use the `hook_post_draw` parameter to make this function run after `post_draw()` instead of `draw()`. This is important when using Processing libraries that support `post_draw()` such as Camera3D or ColorBlindness.

## Signatures

```python
save_frames(
    dirname: str,  # directory to save the frames
    *,
    filename: str = "frame_####.png",  # filename template to use for saved frames
    period: float = 0.0,  # time in seconds between Sketch snapshots (default 0 means no delay)
    start: int = None,  # frame starting number instead of Sketch frame_count
    limit: int = 0,  # limit the number of frames to save (default 0 means no limit)
    sketch: Sketch = None,  # running Sketch
    hook_post_draw: bool = False,  # attach hook to Sketch's post_draw method instead of draw
    block: bool = False  # method returns immediately (False) or blocks until function returns (True)
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
