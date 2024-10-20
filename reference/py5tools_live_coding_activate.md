# py5_tools.live_coding.activate()

Start live coding from a Jupyter Notebook.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import py5_tools

py5_tools.live_coding.activate(
    activate_keyboard_shortcuts=True,
    archive_dir="screenshots",
)
```

</div></div>

</div>

## Description

Start live coding from a Jupyter Notebook. This function should only be called from Jupyter. This will start a Sketch using the code in the executed notebook cells. As more notebook cells are executed, this will keep the Sketch updated with the most recently executed code.

The `always_on_top` parameter will keep the Sketch window on top, above your browser window. This will let you write code in the notebook without interfering with the Sketch window.

The `always_rerun_setup` will rerun the Sketch's current `setup()` function each time a notebook cell is updated, even if the `setup()` function did not change. Be aware this update feature will be triggered even if the executed code has nothing to do with py5.

The `activate_keyboard_shortcuts` will activate convenient keyboard shortcuts for quickly creating screenshots and code archives. These will be saved to an `archive` subdirectory, unless the `archive_dir` parameter sets the save directory to another location.

Look at the online ["Live Coding"](/content/live_coding) documentation to learn more.

## Signatures

```python
activate(
    *,
    always_rerun_setup: bool = True,  # always rerun setup() function when updating code
    always_on_top: bool = True,  # keep Sketch window on top of other windows
    activate_keyboard_shortcuts: bool = False,  # activate keyboard shortcuts for creating screenshots and code archives
    archive_dir: str = "archive"  # directory to save screenshots
) -> None
```

Updated on October 20, 2024 01:40:52am UTC
