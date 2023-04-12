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

## Simple Hybrid Programming Example

Imagine you want your py5 Sketch to draw ten thousand randomly colored points to the screen. To accomplish this, you might write the following code:

```python
def setup():
    py5.size(500, 500, py5.P2D)


def draw():
    for _ in range(10000):
        py5.stroke(py5.random_int(255), py5.random_int(255), py5.random_int(255))
        py5.point(py5.width * py5.random(), py5.height * py5.random())
```

On my computer, this Sketch has a frame rate of 11 fps.

The `draw()` function can be immediately optimized with numpy and more efficient py5 code:

```python
import numpy as np

N = 10000

def draw():
    colors = 255 * np.random.rand(N, 3)
    points = np.random.rand(N, 2) * [py5.width, py5.height]
    with py5.begin_shape(py5.POINTS):
        for i in range(N):
            py5.stroke(*colors[i])
            py5.vertex(*points[i])
```

On my computer, the frame rate increases to 31 fps.

Now let's use hybrid programming to make this even faster. Use the `py5utils` command line tool to create a `Py5Utilities` template and then add the following Java code:

```java
package py5utils;

import py5.core.Sketch;

public class Py5Utilities {

  public Sketch sketch;

  public Py5Utilities(Sketch sketch) {
    this.sketch = sketch;
  }

  public void drawColoredPoints(int[][] colors, float[][] coords) {
    sketch.pushStyle();
    sketch.beginShape(Sketch.POINTS);
    for (int i = 0; i < colors.length; i++) {
      sketch.stroke(colors[i][0], colors[i][1], colors[i][2]);
      sketch.vertex(coords[i][0], coords[i][1]);
    }
    sketch.endShape();
    sketch.popStyle();
  }

}
```

Create the jar file with `mvn -f java package`. The for loop in the previous `draw()` method can be replaced with `py5.utils.drawColoredPoints(colors, points)`.

```python
N = 10000

def draw():
    colors = (255 * np.random.rand(N, 3)).astype(np.int32)
    points = np.random.rand(N, 2).astype(np.float32) * [py5.width, py5.height]
    py5.utils.drawColoredPoints(colors, points)
```

On my computer, the frame rate of this hybrid code is 60 fps.

## Java and Python Object Conversion

Before continuing, we must observe the implicit conversion of Python objects to Java objects when they are passed from Python to Java. In the previous example, the numpy arrays `colors` and `points` were passed to a method that accepts 2D Java arrays of ints and floats. This works because JPype will automatically convert numpy arrays to Java arrays when numpy arrays are passed to a Java method. In addition to this builtin functionality, py5 adds its own conversion rules to convert py5 objects to Processing objects when py5 objects are passed to Java. There are also conversion rules for Processing objects that are passed from Java back to Python. All object conversions are done without any programming burden placed on the end user.

Below is a table of the supported object conversion rules:

TODO: insert table

TODO: say something about the astype() stuff above

## Advanced Hybrid Programming Optimization

Further optimizations of colored points example are still possible. One performance issue comes from the time it takes to copy the numpy arrays from Python's memory space over to Java. This issue can be addressed by sharing memory between Python and Java. Another performance issue comes from creating a new `PShape` object for every call to `drawColoredPoints()`. (This is happening internally in the Processing Library when `sketch.beginShape(Sketch.POINTS)` is called.) This can be addressed by creating the shape once with `createShape()` and updating the vertices' colors and coordinates in each call to `drawColoredPoints()`.
