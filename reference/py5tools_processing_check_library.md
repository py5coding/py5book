# py5_tools.processing.check_library()

Check if a Processing library has been downloaded and stored by py5.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import py5_tools

if py5_tools.processing.check_library("PeasyCam"):
    print("PeasyCam is in your stored library")
```

</div></div>

</div>

## Description

Check if a Processing library has been downloaded and stored by py5. These are the same libraries available to you in the Library Manager when you use the Processing Development Environment (PDE). Downloaded libraries are available for you to import in Python after you import py5.

Downloaded libraries will be saved in the Processing library storage directory. Use [](py5tools_processing_library_storage_dir) to get the specific location of the storage directory on your machine.

## Signatures

```python
check_library(
    library_name: str,  # name of Processing library
) -> bool
```

Updated on April 18, 2025 15:38:01pm UTC
