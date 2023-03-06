# finished

Boolean variable reflecting if the Sketch has stopped permanently.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import time

def draw():
    py5.rect(py5.random_int(py5.width), py5.random_int(py5.height), 10, 10)


py5.run_sketch()
py5.println('sketch has stopped:', py5.finished)
time.sleep(10)

py5.exit_sketch()
py5.println('sketch has stopped:', py5.finished)
```

</div></div>

</div>

## Description

Boolean variable reflecting if the Sketch has stopped permanently.

Underlying Processing field: finished

Updated on March 06, 2023 02:49:26am UTC
