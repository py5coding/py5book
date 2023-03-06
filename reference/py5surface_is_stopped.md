# Py5Surface.is_stopped()

Determine if the surface is currently running an animation.

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
```

</div></div>

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.fill(255, 0, 0)
    py5.rect(50, 50, 10, 10)

py5.run_sketch(block=False)
surface = py5.get_surface()
# this will print True
py5.println(surface.is_stopped())
```

</div></div>

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

Determine if the surface is currently running an animation. A Sketch that has called [](sketch_no_loop) or has no `draw()` function is not animating, and will result in this method returning `True`. If there is a `draw()` function and [](sketch_no_loop) has not been called, this will return `False`. Calling Py5Surface's [](py5surface_stop_thread) will make all future calls to `is_stopped()` return `True`.

The output of this method is independent of [](py5surface_pause_thread) and [](py5surface_resume_thread).

Underlying Processing method: PSurface.isStopped

## Signatures

```python
is_stopped() -> bool
```

Updated on March 06, 2023 02:49:26am UTC
