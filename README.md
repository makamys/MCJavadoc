# MCJavadoc

This repo hosts Minecraft Forge 1.7.10-10.13.4.1614's javadoc, modified to contain some additional bits of documentation (not much at the moment). The instructions used to apply the modifications can be found in the `extra` directory. They are applied by [ExtraJavadoc](https://github.com/makamys/ExtraJavadoc).

## Javadoc links

[**1.7.10-10.13.4.1614**](https://makamys.github.io/MCJavadoc/forge-1.7.10-10.13.4.1614/)

## Building

To generate the javadoc, run `build.py`. This has the following prerequesites:
* Python 3 must be installed
* Java must be installed, and `java` and `javadoc` must be on the PATH
* You need a copy of Forge's decompiled and patched Minecraft source in extracted form. On Windows 10 the JAR can be found at `C:\Users\<name>\.gradle\caches\minecraft\net\minecraftforge\forge\1.7.10-10.13.4.1614-1.7.10\forgeSrc-1.7.10-10.13.4.1614-1.7.10-sources.jar`.
* You need a build of ExtraJavadoc on your computer

## License
Excluding the javadoc output (the `docs` directory), this repository is licensed under the Unlicense.
