# py5_tools.get_classpath()

Get the Java classpath.

## Examples

<div class="example-table">

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

Get the Java classpath. If the JVM has not yet started, this will list the jars that have been added with [](py5tools_add_classpath) and [](py5tools_add_jars). After the JVM has started, the classpath cannot be changed and the aformentioned functions would throw a `RuntimeError`. Use [](py5tools_is_jvm_running) to first determine if the JVM is running.

## Signatures

```python
get_classpath() -> str
```

Updated on March 06, 2023 02:49:26am UTC
