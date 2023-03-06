# second()

Py5 communicates with the clock on your computer.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def draw():
    py5.background(204)
    s = py5.second()  # values from_ 0 - 59
    m = py5.minute()  # values from_ 0 - 59
    h = py5.hour()    # values from_ 0 - 23
    py5.line(s, 0, s, 33)
    py5.line(m, 33, m, 66)
    py5.line(h, 66, h, 100)
```

</div></div>

</div>

## Description

Py5 communicates with the clock on your computer. The `second()` function returns the current second as a value from 0 - 59.

Underlying Processing method: [second](https://processing.org/reference/second_.html)

## Signatures

```python
second() -> int
```

Updated on March 06, 2023 02:49:26am UTC
