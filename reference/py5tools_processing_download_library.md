# py5_tools.processing.download_library()

Download and store a Processing library.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import py5_tools

# this only needs to be run once
py5_tools.processing.download_library("PeasyCam")

import py5

from peasy import PeasyCam

def setup():
    py5.size(500, 500, py5.P3D)
    PeasyCam(py5.get_current_sketch(), 500)


def draw():
    py5.background(128)
    py5.box(200)
```

</div></div>

</div>

## Description

Download and store a Processing library. These are the same libraries available to you in the Library Manager when you use the Processing Development Environment (PDE). After this function downloads a Processing library, it will be available for you to import in Python after you import py5.

This function will also return a dictionary containing some basic information about the installed library. If the library was previously downloaded, it will check the version numbers and will update the library if it is not current. If you want to remove an installed library, use [](py5tools_processing_remove_library).

Downloaded libraries will be saved in the Processing library storage directory. Use [](py5tools_processing_library_storage_dir) to get the specific location of the storage directory on your machine.

## Signatures

```python
download_library(
    library_name: str,  # name of Processing library
) -> dict
```

Updated on May 07, 2025 18:32:23pm UTC
