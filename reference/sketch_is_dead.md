# is_dead

Boolean value reflecting if the Sketch has been run and has now stopped.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import time

def setup():
    py5.background(255, 0, 0)


print("the sketch is ready:", py5.is_ready)

py5.run_sketch(block=False)

print("the sketch is running:", py5.is_running)

py5.exit_sketch()

# wait for exit_sketch to complete
time.sleep(1)

print("the sketch is dead:", py5.is_dead)
print("did the sketch exit from an error?", py5.is_dead_from_error)
```

</div></div>

</div>

## Description

Boolean value reflecting if the Sketch has been run and has now stopped. This will be `True` after calling [](sketch_exit_sketch) or if the Sketch throws an error and stops. This will also be `True` after calling [](py5surface)'s [](py5surface_stop_thread) method. Once a Sketch reaches the "dead" state, it cannot be rerun.

After an error or a call to [](py5surface_stop_thread), the Sketch window will still be open. Call [](sketch_exit_sketch) to close the window.

Updated on December 25, 2023 17:40:34pm UTC
