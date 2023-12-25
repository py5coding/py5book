# is_ready

Boolean value reflecting if the Sketch is in the ready state.

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

Boolean value reflecting if the Sketch is in the ready state. This will be `True` before [](sketch_run_sketch) is called. It will be `False` while the Sketch is running and after it has exited.

Updated on December 25, 2023 17:40:34pm UTC
