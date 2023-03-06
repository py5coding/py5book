# millis()

Returns the number of milliseconds (thousandths of a second) since starting the program.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def draw():
    m = py5.millis()
    py5.no_stroke()
    py5.fill(m%255)
    py5.rect(25, 25, 50, 50)
```

</div></div>

</div>

## Description

Returns the number of milliseconds (thousandths of a second) since starting the program. This information is often used for timing events and animation sequences.

Underlying Processing method: [millis](https://processing.org/reference/millis_.html)

## Signatures

```python
millis() -> int
```

Updated on March 06, 2023 02:49:26am UTC
