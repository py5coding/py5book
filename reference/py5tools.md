# Py5 Tools

The py5 Tools are extra utility functions not directly related to creating Sketches that help faciliate the use of py5.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import py5_tools

print(py5_tools.get_jvm_debug_info())
```

</div></div>

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import py5_tools

py5_tools.add_jars('path/to/project_jars')
py5_tools.add_classpath('path/to/jar/file/java_code.jar')

import py5

py5.println(py5_tools.get_classpath())
```

</div></div>

</div>

## Description

The py5 Tools are extra utility functions not directly related to creating Sketches that help faciliate the use of py5. For example, you can use these to add jar files to the Java classpath before importing py5. All of the py5 Tools are in the Python package `py5_tools`, which are installed alongside py5 but must be explicitly imported before using them. The `py5_tools` package is imported for you when coding in [imported mode](content-py5-modes-imported-mode) such as with the py5 Jupyter Notebook kernel.

The following functions are provided:

```{include} include_py5tools.md
```

Updated on March 18, 2024 05:08:14am UTC
