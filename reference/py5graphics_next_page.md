# Py5Graphics.next_page()

Move to the next page in a PDF document.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.size(600, 600, py5.PDF, "/tmp/test.pdf")


def draw():
    for _ in range(50):
        py5.rect(py5.random_int(py5.width), py5.random_int(py5.height), 10, 10)

    if py5.frame_count < 5:
        py5.g.next_page()
    else:
        py5.exit_sketch()
```

</div></div>

</div>

## Description

Move to the next page in a PDF document. This method is only available when using a `PDF` [](py5graphics) object. Using this method with any other graphics renderer will result in an error.

Underlying Processing method: PGraphics.nextPage

## Signatures

```python
next_page() -> None
```

Updated on March 06, 2023 02:49:26am UTC
