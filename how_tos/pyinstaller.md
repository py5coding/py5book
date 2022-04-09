# How to Create PyInstaller Packages

stuff

[PyInstaller](https://pyinstaller.readthedocs.io/en/stable/) is a widely used Python tool for bundling a Python package into a
single sharable, distributable package. This page shows you how to create a
PyInstaller package for a py5 Sketch.

PyInstaller will attempt to analyze a Python script and figure out what Python libraries need
to be included in the package. For complex applications, the default analysis might miss some
necessary Python libraries, binary files, or data files. Since py5 is using Java, there are
some packaging customizations that need to be addressed with supporting PyInstaller library code.

```python
from PyInstaller.utils.hooks import collect_submodules, collect_dynamic_libs, collect_data_files
datas, binaries, hiddenimports = [], [], []
```

```python
datas += [('/usr/lib/jvm/java-17-openjdk', 'JAVA_HOME')]
```

```python
binaries += collect_dynamic_libs('py5')
```

```python
binaries += filter(lambda x: x[1].split('/')[2] in ["linux-amd64"], collect_dynamic_libs('py5'))
```

```python
datas += collect_data_files('py5', includes=['**/*.jar'])
datas += collect_data_files('py5_tools')
```

https://github.com/pyinstaller/pyinstaller/issues/5363

```python
hiddenimports += collect_submodules('xmlrpc')
datas += collect_data_files('debugpy')
```

```python
datas += [('simple.py', '.')]
```
