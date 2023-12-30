# select_folder()

Opens a file chooser dialog to select a folder.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def folder_selected(selection):
    if selection is None:
        py5.println("Window was closed or the user hit cancel.")
    else:
        py5.println("User selected " + selection)


def setup():
    py5.select_folder("Select a folder to process:", folder_selected)
```

</div></div>

</div>

## Description

Opens a file chooser dialog to select a folder. After the selection is made, the selection will be passed to the `callback` function. If the dialog is closed or canceled, `None` will be sent to the function, so that the program is not waiting for additional input. The callback is necessary because of how threading works.

This method has some platform specific quirks. On macOS, this does not work when the Sketch is run through a Jupyter notebook. On Windows, Sketches using the OpenGL renderers (`P2D` or `P3D`) will be minimized while the select dialog box is open. This method only uses native dialog boxes on macOS.

Underlying Processing method: [selectFolder](https://processing.org/reference/selectFolder_.html)

## Signatures

```python
select_folder(
    prompt: str,  # text prompt for select dialog box
    callback: Callable,  # callback function after selection is made
    default_folder: str = None,  # default folder
) -> None
```

Updated on December 27, 2023 13:47:02pm UTC
