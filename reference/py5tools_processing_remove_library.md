# py5_tools.processing.remove_library()

Remove a previously downloaded and stored Processing library.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import py5_tools

py5_tools.processing.remove_library("PeasyCam")
```

</div></div>

</div>

## Description

Remove a previously downloaded and stored Processing library. These are the same libraries available to you in the Library Manager when you use the Processing Development Environment (PDE). You download and install Processing libraries with [](py5tools_processing_download_library). After this function removes a Processing library, it will no longer be available for you to use with py5.

## Signatures

```python
remove_library(
    library_name: str,  # name of Processing library
) -> None
```

Updated on May 07, 2025 18:32:23pm UTC
