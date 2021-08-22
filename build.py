import subprocess
import sys
import os
from pathlib import Path

if len(sys.argv) != 4:
    sys.exit("Usage: {} EXTRA_JAVADOC_JAR SRCDIR EXTRA_JSON".format(sys.argv[0]))

cwd = Path(os.getcwd())

EXTRA_JAVADOC_JAR, SRCDIR, EXTRA_JSON = sys.argv[1:]

dirName = Path(SRCDIR).name
outJavadocDir = cwd / "www" / dirName
outSrcDir = cwd / "build/src"

os.makedirs(outSrcDir, exist_ok=True)
os.makedirs(outJavadocDir, exist_ok=True)

os.chdir(outSrcDir)
subprocess.run(["java", "-jar", EXTRA_JAVADOC_JAR, SRCDIR, EXTRA_JSON])
os.chdir(outJavadocDir)

subprocess.run(["javadoc", "-sourcepath", outSrcDir / dirName, "-subpackages", "."])