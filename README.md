# MCJavadoc

This repo hosts Minecraft Forge 1.7.10-10.13.4.1614's Javadoc, modified to contain some additional bits of documentation (not much at the moment). The instructions used to apply the modifications can be found in the `extra` directory. They are applied by [ExtraJavadoc](https://github.com/makamys/ExtraJavadoc).

## Browse the Javadoc

* [Index](https://makamys.github.io/MCJavadoc/)
  * [**1.7.10-10.13.4.1614**](https://makamys.github.io/MCJavadoc/forge-1.7.10-10.13.4.1614/)

## Building

Prerequisites: Java 8, Python 3, Pandoc.

Run `python3 build.py`. This will build ExtraJavadoc from source, then build the RFG example mod, then use ExtraJavadoc to augment the decompiled sources, and finally use `javadoc` to generate the javadoc.

Only Java 8 is supported. The Java version can be overridden by setting the `JAVA_HOME` environmental variable.

## License
Excluding the Javadoc output (the `docs` directory), this repository is licensed under the Unlicense.
