# py5_tools.offline_frame_processing()

Process Sketch frames in a separate thread that will minimize the performance impact on the Sketch's main animation thread.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import skvideo.io
import py5_tools


py5.run_sketch(block=False)

writer = skvideo.io.FFmpegWriter(
    '/tmp/video.mp4',
    inputdict={'-r': str(30)},
    outputdict={'-vcodec': 'libx264', '-pix_fmt': 'yuv420p', '-r': str(30)}
)

py5_tools.offline_frame_processing(writer.writeFrame, limit=60 * 30,
                                   complete_func=writer.close)
```

</div></div>

</div>

## Description

Process Sketch frames in a separate thread that will minimize the performance impact on the Sketch's main animation thread. As the Sketch runs it will place a numpy array of the frame's pixels in a queue that will be later passed to the user provided processing function (the `func` parameter). That function should not call any Sketch methods. The `offline_frame_processing()` functionality is well suited for goals such as live-streaming to YouTube or encoding a video file, both of which might otherwise impact the Sketch's frame rate significantly.

The user provided processing function must take a single numpy array as a parameter. That numpy array will have a shape of `(batch size, height, width, 3)` and have a dtype of `np.uint8`. The `batch_size` parameter defaults to 1 but can be set to other values to stack frames together into a larger array. Therefore a "batch" will consist of one or more frames.

Use the `limit` parameter to stop frame processing after a set number of frames. You can also use the `stop_processing_func` parameter to provide a callable that returns `True` when processing should complete (which will stop right away and ignore unprocessed frames in the queue). Use the `complete_func` parameter to pass a function that will be called once after frame processing has stopped.

The `queue_limit` parameter specifies a maximum queue size. If frames are added to the queue faster than they can be processed, the queue size will grow unbounded. Setting a queue limit will cause the oldest frames on the queue to be dropped, one batch at a time. You can use the `period` parameter to pause between frames that are collected for processing, throttling the workload.

By default this function will return right away and will process frames in the background while the Sketch is running. Set the `block` parameter to `True` to instruct the method to not return until the processing is complete or the Sketch terminates. This blocking feature is not available on macOS when the Sketch is executed through an IPython kernel.

By default this function will report its progress as frames are processed. If you are using a Jupyter Notebook and happen to be processing tens of thousands of frames, this might cause Jupyter to crash. To avoid that fate, set the `display_progress` parameter to `False`.

Use the `sketch` parameter to specify a different running Sketch, such as a Sketch created using Class mode. If your Sketch has a `post_draw()` method, use the `hook_post_draw` parameter to make this function run after `post_draw()` instead of `draw()`. This is important when using Processing libraries that support `post_draw()` such as Camera3D or ColorBlindness.

## Signatures

```python
offline_frame_processing(
    func: Callable[[npt.NDArray[np.uint8]], None],  # function to process the Sketch's pixels, one batch at a time
    *,
    limit: int = 0,  # total number of frames to pass to the frame processing function
    period: float = 0.0,  # time in seconds between frames collected to be passed to the frame processing function (default 0 means no delay)
    batch_size: int = 1,  # number of frames to include in each batch passed to the frame processing function
    complete_func: Callable[[], None] = None,  # function to call when frame processing is complete
    stop_processing_func: Callable[[], bool] = None,  # optional predicate function that determines if frame processing should terminate
    sketch: Sketch = None,  # running Sketch
    hook_post_draw: bool = False,  # attach hook to Sketch's post_draw method instead of draw
    queue_limit: int = None,  # maximum number of frames that can be on the queue waiting to be processed
    block: bool = False,  # method returns immediately (False) or blocks until function returns (True)
    display_progress: bool = True  # display progress as frames are processed
) -> None
```

Updated on February 27, 2024 16:53:28pm UTC
