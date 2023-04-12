# Hybrid Programming

Hybrid Programming refers to py5's ability to augment your py5 Sketch code with Java. This is very much like creating custom Processing extensions to enhance py5.

## Reasons for Hybrid Programming

There are a few reasons why your coding projects might benefit from hybrid programming.

First, performance. This is the most important benefit. Although py5 Sketches can provide excellent performance, you may experience performance problems if you have a large or nested for loop making many calls from Python to Java. There is a small microsecond performance penalty for each individual call from Python to Java. This can accumulate to something significant in large or nested for loops. Hybrid programming can enable you to pass a large amount of data to Java with one call, where you can then iterate through the data without the performance penalty.

The second reason is that hybrid programming opens a door to incorporating Java libraries into your work. Much like Python, the Java library ecosystem is extensive and backed by a strong community. If you can't find the library you need in the Python world, the Java world might have what you need.

The third benefit of hybrid programming is how it can add the simplicity and prototyping strengths of Python to the development process of a Java Processing Sketch. This is true even if the final output will ultimately be 100% Java.

## Understand JPype

Before exploring hybrid programming in py5, you should first read JPype's documentation. Being knowledgeable about JPype will help you accomplish more with hybrid programming. Start with the [Java QuickStart Guide](https://jpype.readthedocs.io/en/latest/quickguide.html). Also read the [Working with Numpy](https://jpype.readthedocs.io/en/latest/userguide.html#working-with-numpy) and [Implementing Java interfaces](https://jpype.readthedocs.io/en/latest/userguide.html#implementing-java-interfaces) sections in the [JPype User Guide](https://jpype.readthedocs.io/en/latest/userguide.html).

## Importing Java Classes into Python

Technically you don't really need much from py5 to combine Python and Java code because JPype already provides most of the functionality. As explained in JPype's documentation, you can seamlessly import any Java class and create instances. To do this, you must do two things.

1. Add the necessary jar files to your classpath *before* importing py5. There are a few ways you can do this:
   * Explicitly adding the jars with [](/reference/py5tools_add_jars) or [](/reference/py5tools_add_classpath)
   * Place your jar files in a `jars` directory that is a subdirectory of the current working directory
   * Create an environment variable `PY5_JARS` that points to a directory with jar files
2. Import the Java libraries with the `import` command *after* importing py5. Importing py5 will also start the JVM. Jars cannot be added after the JVM is started.

A simple example might look like this:

```python
from pathlib import Path

import py5_tools

# import project specific jar files in `project_jar_dir`
py5_tools.add_jars(Path.home() / 'project_jar_dir')

import py5

from java.lang import String
# import Java class JavaUtilities
from org.utils import JavaUtilities

test_string = String('test')
# create instance of JavaUtilities class
utils = JavaUtilities()
```

## Hybrid Programming Support in py5

The py5 installation comes with the `py5utils` command line utility for setting up a framework for hybrid coding.

```bash
$ py5utils -h
usage: py5utils [-h] [-o OUTPUT_DIR]

Generate Py5Utilities framework

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_DIR, --output OUTPUT_DIR
                        output destination (defaults to current directory)
```

Running the utility creates some files and directories:

```bash
$ py5utils
$ tree .
.
├── jars
└── java
    ├── pom.xml
    └── src
        └── main
            └── java
                └── py5utils
                    └── Py5Utilities.java

7 directories, 2 files
```

The `Py5Utilities.java` file contains this code:

```java
package py5utils;

import py5.core.Sketch;

public class Py5Utilities {

  public Sketch sketch;

  public Py5Utilities(Sketch sketch) {
    this.sketch = sketch;
  }

}
```

Compile the code with the Maven command `mvn -f java package` to create `py5utilities.jar` in the `jars` directory.

When py5 runs a Sketch, it will attempt to create an instance of `py5utils.Py5Utilities`. If successful, it will add the instance to `py5.utils` (or `self.utils` for coders using py5's class mode) for you to interact with in your code. If `py5utils.Py5Utilities` cannot be created, the `utils` attribute will be `None`.

Below is a simple illustrative example:

```java
package py5utils;

import py5.core.Sketch;

public class Py5Utilities {

  public Sketch sketch;

  public Py5Utilities(Sketch sketch) {
    this.sketch = sketch;
  }

  public void drawColoredPoints(int[] colors, float[][] coords) {
    sketch.beginShape();
    sketch.pushStyle();
    for (int i = 0; i < colors.length; i++) {
        sketch.stroke(colors[i]);
        sketch.vertex(coords[i][0], coords[i][1]);
    }
    sketch.popStyle();
    sketch.endShape();
  }

}
```


## Java and Python Object Conversion

Py5Image to PImage

Strings

## Performance Testing

Illustrative example using colored points

Show line profiler
