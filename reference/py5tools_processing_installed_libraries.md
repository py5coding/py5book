# py5_tools.processing.installed_libraries()

List the Processing libraries stored in your computer's Processing library storage directory.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import py5_tools

print(py5_tools.processing.installed_libraries())
# ['Camera 3D', 'PeasyCam', 'ColorBlindness']
```

</div></div>

</div>

## Description

List the Processing libraries stored in your computer's Processing library storage directory. These are all of the Processing libraries that have been installed using the [](py5tools_processing_download_library) function. To get the location of the library storage directory, use the [](py5tools_processing_library_storage_dir) function.

Downloaded libraries will be saved in the Processing library storage directory. Use [](py5tools_processing_library_storage_dir) to get the specific location of the storage directory on your machine.

## Signatures

```python
installed_libraries() -> list[str]
```

Updated on April 18, 2025 05:23:11am UTC
