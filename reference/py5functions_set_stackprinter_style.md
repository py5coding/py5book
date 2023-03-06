# set_stackprinter_style()

Set the formatting style for py5's stack traces.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import py5
py5.set_stackprinter_style('lightbg')
```

</div></div>

</div>

## Description

Set the formatting style for py5's stack traces. Py5 uses the Python library stackprinter to show exception stack traces. The stackprinter library supports various color styles. By default py5 will use `'plaintext'`, which does not use color. Alternative styles using color are `'darkbg'`, `'darkbg2'`, `'darkbg3'`, `'lightbg'`, `'lightbg2'`, and `'lightbg3'`.

## Signatures

```python
set_stackprinter_style(
    style: str,  # name of stackprinter style
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
