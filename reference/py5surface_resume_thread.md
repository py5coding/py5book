# Py5Surface.resume_thread()

Resume a paused Sketch.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def draw():
    py5.rect(py5.random(py5.width), py5.random(py5.height), 10, 10)
    py5.println(py5.frame_count)

py5.run_sketch(block=False)
surface = py5.get_surface()

# pause the sketch.
surface.pause_thread()
# the sketch is no longer running and there is no output

# after waiting a bit, resume the sketch
surface.resume_thread()
```

</div></div>

</div>

## Description

Resume a paused Sketch. The Sketch window will resume operating as it did before [](py5surface_pause_thread) was called.

The [](sketch_frame_count) will continue incrementing after the Sketch is resumed.

Underlying Processing method: PSurface.resumeThread

## Signatures

```python
resume_thread() -> None
```

Updated on March 06, 2023 02:49:26am UTC
