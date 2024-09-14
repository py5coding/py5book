# py5_tools.live_coding.copy_code()

Create a backup copy of the current code.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import py5_tools

py5_tools.live_coding.screenshot("version_%H%M%S")
py5_tools.live_coding.copy_code("version_%H%M%S")
```

</div></div>

</div>

## Description

Create a backup copy of the current code. The copy will be saved to the archive directory. By default, this is an `archive` subdirectory under the Sketch code's current working directory.

If the `copy_name` parameter contains date format codes, the string will be formatted with the current timestamp. If `copy_name` is omitted, it will default to your filename stem followed by `"_%Y%m%d_%H%M%S"`.

This function will not work if the live coding feature is being used in a Jupyter Notebook. If live coding is watching the directory for changes, the backup copy will be a zip file containing every file in the watched directory. Otherwise, it will be a regular Python file. The appropriate filename suffix will be set if `copy_name` does not already have it. It won't overwrite an existing file if the file it tries to write to already exists.

A suggested use case for this is to put the function calls in your code but leave them commented out. When you have working code that you want to create a backup for but don't want to pause your workflow to do that manually, simply uncomment the code and resave the file. A copy of the code will then be created for you in the `archive` subdirectory.

This function will do nothing when not running through py5's live coding feature.

Look at the online ["Live Coding"](/content/live_coding) documentation to learn more.

## Signatures

```python
copy_code(
    copy_name: str = None,  # name of file for copy of code
) -> None
```

Updated on September 14, 2024 20:36:29pm UTC
