# launch_repeating_thread()

Launch a new thread that will repeatedly execute a function in parallel with your Sketch code.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def pick_color():
    global color
    color = py5.random_int(255), py5.random_int(255), py5.random_int(255)


def setup():
    py5.launch_repeating_thread(pick_color, name='pick_color', time_delay=1)


def draw():
    py5.background(*color)
    if py5.frame_count == 500:
        py5.stop_thread('pick_color')
```

</div></div>

</div>

## Description

Launch a new thread that will repeatedly execute a function in parallel with your Sketch code. This can be useful for executing non-py5 code that would otherwise slow down the animation thread and reduce the Sketch's frame rate.

Use the `time_delay` parameter to set the time in seconds between one call to function `f` and the next call. Set this parameter to `0` if you want each call to happen immediately after the previous call finishes. If the function `f` takes longer than expected to finish, py5 will wait for it to finish before making the next call. There will not be overlapping calls to function `f`.

The `name` parameter is optional but useful if you want to monitor the thread with other methods such as [](sketch_has_thread). If the provided `name` is identical to an already running thread, the running thread will first be stopped with a call to [](sketch_stop_thread) with the `wait` parameter equal to `True`.

Use the `args` and `kwargs` parameters to pass positional and keyword arguments to the function.

Use the `daemon` parameter to make the launched thread a daemon that will run without blocking Python from exiting. This parameter defaults to `True`, meaning that function execution can be interupted if the Python process exits. Note that if the Python process continues running after the Sketch exits, which is typically the case when using a Jupyter Notebook, this parameter won't have any effect unless if you try to restart the Notebook kernel. Generally speaking, setting this parameter to `False` causes problems but it is available for those who really need it. See [](sketch_stop_all_threads) for a better approach to exit threads.

The new thread is a Python thread, so all the usual caveats about the Global Interpreter Lock (GIL) apply here.

## Signatures

```python
launch_repeating_thread(
    f: Callable,  # function to call in the launched thread
    name: str = None,  # name of thread to be created
    *,
    time_delay: float = 0,  # time delay in seconds between calls to the given function
    daemon: bool = True,  # if the thread should be a daemon thread
    args: tuple = None,  # positional arguments to pass to the given function
    kwargs: dict = None  # keyword arguments to pass to the given function
) -> str
```

Updated on March 06, 2023 02:49:26am UTC
