# window_title()

Set the Sketch window's title.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.size(200, 200)
    py5.window_title("py5 window")
```

</div></div>

</div>

## Description

Set the Sketch window's title. This will typically appear at the window's title bar. The default window title is "Sketch".

This method provides the same functionality as [](py5surface_set_title) but without the need to interact directly with the [](py5surface) object.

Underlying Processing method: windowTitle

## Signatures

```python
window_title(
    title: str,  # new window title
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
