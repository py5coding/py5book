# py5_tools.processing.library_storage_dir()

Return the location of the Processing library storage directory.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
print(py5_tools.processing.library_storage_dir())
# /home/jim/.cache/py5/processing-libraries
```

</div></div>

</div>

## Description

Return the location of the Processing library storage directory. You should never need to manually edit files in this directory, but if for some reason you do, you'll first need to find it. By default, this will be in `~/.cache/py5` on Linux and MacOS machines and `~/AppData/Local/py5` on Windows machines. These locations are similar to where other Python libraries store their data files. If you wish, set the `PY5_HOME` environment variable to move the storage directory to a location of your choosing.

If you wish to manually add Java Jar files to py5's classpath, don't use this directory. Instead, put jars in a `jars` subdirectory (relative to the current working directory of your Python code) or set the `PY5_JARS` environment variable to the path of the directory you wish to use.

## Signatures

```python
library_storage_dir() -> Path
```

Updated on April 18, 2025 05:23:11am UTC
