# How to Create PyInstaller Packages

[PyInstaller](https://pyinstaller.readthedocs.io/en/stable/) is a widely used
Python tool for bundling a Python package into a single sharable, distributable
package. This page shows you how to create a PyInstaller package for a py5
Sketch.

PyInstaller will attempt to analyze Python code and figure out what Python
libraries need to be included in the package. For complex applications, the
default analysis might miss some necessary Python libraries, binary files, or
data files. Since py5 is using Java, there will be some packaging customizations
that need to be addressed with the PyInstaller utilities.

## PyInstaller Spec File Explanation

See this gist if you want to start with a [working PyInstaller example](https://gist.github.com/hx2A/da84f59794196c59d1b67166bc324cd1).
For a line by line explanation, read the rest of this page. The below example
Spec File will create an application called `simple` from a py5 Sketch
implemented in the Python file `simple.py`. Typically you would put this in a
Spec File named `simple.spec` and run it at the command line with:

```bash
pyinstaller simple.spec
```

Now, on to the contents of the Spec File.

### Imports

First, import a few utility functions from `PyInstaller`. We will use these to
gather information on the Python libraries, binary files, or data files that
PyInstaller would otherwise miss.

```python
from PyInstaller.utils.hooks import collect_submodules, collect_dynamic_libs, collect_data_files
datas, binaries, hiddenimports = [], [], []
```

### Java Runtime Environment

The py5 library requires Java to be installed on all users' machines. If you
want to include the Java Runtime Environment in the PyInstaller Package, you
will need to locate Java on your machine and add the path to `datas`, similar
to the following:

```python
datas += [('/usr/lib/jvm/java-17-openjdk', 'JAVA_HOME')]
```

Note that the `'JAVA_HOME'` you see here has nothing to do with the `JAVA_HOME`
environment variable. Instead, PyInstaller will copy the contents of
`/usr/lib/jvm/java-17-openjdk` into a new directory named `JAVA_HOME` in the
constructed package. At runtime, py5 will detect that it has been packaged with
PyInstaller and will check for this special `JAVA_HOME` directory. If it is
found, py5 will use that Java installation to run the Sketch.

If you wish, you can skip this step and reduce the final package size by ~25%.
If this `JAVA_HOME` directory is not included in the package, py5 will search
for Java in the usual install locations. The Sketch will run normally if it is
found. Only skip this step if you are confident all of the users you will
distribute your package to already have the proper version of Java installed.
Or, perhaps your Python code is doing something clever with the Python library
[`install-jdk`](https://pypi.org/project/install-jdk/) to install Java on the
machines of your users that don't already have it. You can make your own choices
for how to approach this.

### py5

The Python library py5 contains several Java jar files. These must be explicitly
named to be included in the PyInstaller package.

```python
datas += collect_data_files('py5', includes=['**/*.jar'])
```

The Python library py5 also contains native libraries for OpenGL. These must
also be explicitly named.

```python
binaries += collect_dynamic_libs('py5')
```

The above code will collect the native libraries py5 contains for all supported
platforms. This is a bit excessive because the package PyInstaller creates will
not be able to run on all platforms. If you want to limit the collected native
libraries to only those that are relevant for the package, you can do so with
code similar to the following:

```python
binaries += filter(lambda x: x[1].split('/')[2] in ["linux-amd64"], collect_dynamic_libs('py5'))
```

The below code will collect the py5 logo images, found in `py5_tools`. If this
is omitted, a warning message will be displayed to the console when the Sketch
executes.

```python
datas += collect_data_files('py5_tools')
```

### Sketch Code

Normally PyInstaller packages Python bytecode files, not the actual source
files. However, py5 needs the actual source file if your Sketch calls
[`size()`](../reference/sketch_size) from the `setup()` function.

Technically, [`size()`](../reference/sketch_size) should only be called from a
`settings()` function, but py5 lets you simplify your code and put it in
`setup()` instead. This is conditional on py5 being able to parse your code and
create a `settings()` function on your behalf. To accomplish this, py5 needs
access to the source code for your `setup()` function.

You can skip this step if your py5 Sketch already has a `settings()` function
that calls [`size()`](../reference/sketch_size).

```python
datas += [('simple.py', '.')]
```

### Extra Missing Python Libraries

The Python libraries `xmlrpc` and `debugpy` both have quirks that prevent
PyInstaller from packaging them properly. These two lines of code fix that.

```python
hiddenimports += collect_submodules('xmlrpc')
datas += collect_data_files('debugpy')
```

### Exclude Unnecessary Python Libraries

Sometimes PyInstaller will package Python libraries your application doesn't
actually need. Unless your Sketch explicitly uses these, the following libraries
can be safely excluded. This will reduce the final package size by ~30%. There
might be other libraries that can also be excluded. If package size is a
concern, feel free to experiment.

```python
excludes = ['matplotlib', 'scipy', 'jedi', 'lxml', 'PyQt5']
```

### PyInstaller Package Assembly

The below code is a slight modification of the default PyInstaller generated
Spec File to connect the variables defined above to PyInstaller's `Analysis`
class. Observe the use of the `binaries`, `datas`, `hiddenimports`, and
`excludes` variables.

```python
block_cipher = None

a = Analysis(['simple.py'],
             pathex=[],
             binaries=binaries,
             datas=datas,
             hiddenimports=hiddenimports,
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=excludes,
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
```

If you wish to package your Sketch into one directory, finish your Spec File
with this:

```python
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='simple',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None)

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='simple')
```

To create a single file executable, conclude your Spec File with this instead:

```python
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='simple',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None)
```
