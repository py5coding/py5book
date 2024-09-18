# py5_tools.live_coding.snapshot()

Create a screenshot of the current Sketch window and a backup copy of the current code.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import py5_tools

py5_tools.live_coding.snapshot("version_%H%M%S")
```

</div></div>

</div>

## Description

Create a screenshot of the current Sketch window and a backup copy of the current code. This function combines the functionality of [](py5tools_live_coding_screenshot) and [](py5tools_live_coding_copy_code). Everything will be saved to the archive directory. By default, this is an `archive` subdirectory under the Sketch code's current working directory.

See the documentation for [](py5tools_live_coding_screenshot) and [](py5tools_live_coding_copy_code) for more information about each feature.

If the `snapshot_name` parameter contains date format codes, the string will be formatted with the current timestamp. If `snapshot_name` is omitted, it will default to your filename stem followed by `"_%Y%m%d_%H%M%S"`. If you are using this function through a Jupyter Notebook, there is no useable filename so it will default to `"snapshot_%Y%m%d_%H%M%S"`. Although if you are using this function through a Jupyter Notebook, it will decline to create a backup copy of the code so you are better off using [](py5tools_live_coding_screenshot) instead.

A suggested use case for this is to put the function calls in your code but leave them commented out. When you have working code that you want to create a backup and a screenshot for but don't want to pause your workflow to do both manually, simply uncomment the code and save the file. A backup and a screenshot will then be created for you in the `archive` subdirectory.

This function will do nothing when not running through py5's live coding feature.

Look at the online ["Live Coding"](/content/live_coding) documentation to learn more.

## Signatures

```python
snapshot(
    snapshot_name: str = None,  # name of file for screenshot and code archive
) -> None
```

Updated on September 15, 2024 12:12:36pm UTC
