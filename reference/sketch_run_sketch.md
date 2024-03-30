# run_sketch()

Run the Sketch.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
py5.run_sketch(block=True)
print("this message will not be printed until after the sketch exits")
```

</div></div>

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
py5.run_sketch(block=False)
print("this message will be printed immediately, while the sketch is running")
```

</div></div>

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
# run the sketch with the window at position 400, 300 on display #1
py5.run_sketch(block=False, py5_options=['--location=400,300', '--display=1'], sketch_args=['py5 is awesome'])
# this will print 'py5 is awesome'
print(py5.pargs[0])
```

</div></div>

</div>

## Description

Run the Sketch. Code in the `settings()`, `setup()`, and `draw()` functions will be used to actualize your Sketch.

Use the `block` parameter to specify if the call to `run_sketch()` should return immediately (asynchronous Sketch execution) or block until the Sketch exits. If the `block` parameter is not specified, py5 will first attempt to determine if the Sketch is running in a Jupyter Notebook or an IPython shell. If it is, `block` will default to `False`, and `True` otherwise. However, on macOS, these default values are required, as py5 cannot work on macOS without them.

A list of strings passed to `py5_options` will be passed to the Processing PApplet class as arguments to specify characteristics such as the window's location on the screen. A list of strings passed to `sketch_args` will be available to a running Sketch using [](sketch_pargs). See the third example for an example of how this can be used.

When calling `run_sketch()` in [module mode](content-py5-modes-module-mode), py5 will by default search for functions such as `setup()`,  `draw()`, etc. in the caller's stack frame and use those in the Sketch. If for some reason that is not what you want or does not work because you are hacking py5 to do something unusual, you can use the `sketch_functions` parameter to pass a dictionary of the desired callable functions. The `sketch_functions` parameter is not available when coding py5 in [class mode](content-py5-modes-class-mode). Don't forget you can always replace the `draw()` function in a running Sketch using [](sketch_hot_reload_draw).

When programming in [module mode](content-py5-modes-module-mode) and [imported mode](content-py5-modes-imported-mode), py5 will inspect the `setup()` function and will attempt to split it into synthetic `settings()` and `setup()` functions if both were not created by the user and the real `setup()` function contains calls to [](sketch_size), [](sketch_full_screen), [](sketch_smooth), [](sketch_no_smooth), or [](sketch_pixel_density). Calls to those functions must be at the very beginning of `setup()`, before any other Python code (except for comments). This feature allows the user to omit the `settings()` function, much like what can be done while programming in the Processing IDE. This feature is not available when programming in [class mode](content-py5-modes-class-mode).

When running a Sketch asynchronously through Jupyter Notebook, any `print` statements using Python's builtin function will always appear in the output of the currently active cell. This will rarely be desirable, as the active cell will keep changing as the user executes code elsewhere in the notebook. As an alternative, use py5's [](sketch_println) method, which will place all text in the output of the cell that made the `run_sketch()` call. This will continue to be true if the user moves on to execute code in other Notebook cells. Use [](sketch_set_println_stream) to customize this behavior. All py5 error messages and stack traces are routed through the [](sketch_println) method. Be aware that some error messages and warnings generated inside the Processing Jars cannot be controlled in the same way, and may appear in the output of the active cell or mixed in with the Jupyter Kernel logs.

The `jclassname` parameter should only be used when programming in Processing Mode. This value must be the canonical name of your Processing Sketch class (i.e. `"org.test.MySketch"`). The class must inherit from `py5.core.SketchBase`. To pass parameters to your Processing Sketch class constructor, use the `jclass_params` parameter. Read py5's online documentation to learn more about [Processing Mode](/content/processing_mode).

## Signatures

```python
run_sketch(
    block: bool = None,  # method returns immediately (False) or blocks until Sketch exits (True)
    *,
    py5_options: list[str] = None,  # command line arguments to pass to Processing as arguments
    sketch_args: list[str] = None,  # command line arguments that become Sketch arguments
    sketch_functions: dict[str, Callable] = None,  # sketch methods when using [module mode](content-py5-modes-module-mode)
    jclassname: str = None,  # canonical name of class to instantiate when using py5 in processing mode
    jclass_params: tuple[Any] = ()  # parameters to pass to constructor when using py5 in processing mode
) -> None
```

Updated on March 21, 2024 23:14:19pm UTC
