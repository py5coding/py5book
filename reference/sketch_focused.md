# focused

Confirms if a py5 program is "focused," meaning that it is active and will accept mouse or keyboard input.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    if py5.focused:
        py5.ellipse(25, 25, 50, 50)
    else:
        py5.line(0, 0, 100, 100)
        py5.line(100, 0, 0, 100)
```

</div></div>

</div>

## Description

Confirms if a py5 program is "focused," meaning that it is active and will accept mouse or keyboard input. This variable is `True` if it is focused and `False` if not.

Underlying Processing field: [focused](https://processing.org/reference/focused.html)

Updated on March 06, 2023 02:49:26am UTC
