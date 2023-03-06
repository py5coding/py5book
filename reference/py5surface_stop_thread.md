# Py5Surface.stop_thread()

Stop the animation thread.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def draw():
    py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)

py5.run_sketch(block=False)
surface = py5.get_surface()
# this will print False
py5.println(surface.is_stopped())

surface.stop_thread()
# now it will print True
py5.println(surface.is_stopped())
```

</div></div>

</div>

## Description

Stop the animation thread. The Sketch window will remain open but will be static and unresponsive. Use [](py5surface_is_stopped) to determine if a Sketch has been stopped or not.

This method is different from [](py5surface_pause_thread) in that it will irreversably stop the animation. Use [](py5surface_pause_thread) and [](py5surface_resume_thread) if you want to pause and resume a running Sketch.

Underlying Processing method: PSurface.stopThread

## Signatures

```python
stop_thread() -> bool
```

Updated on March 06, 2023 02:49:26am UTC
