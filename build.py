import subprocess
import sys
import os
from pathlib import Path

if len(sys.argv) != 4:
    sys.exit("Usage: {} EXTRA_JAVADOC_JAR SRCDIR EXTRA_JSON".format(sys.argv[0]))

cwd = Path(os.getcwd())

EXTRA_JAVADOC_JAR, SRCDIR, EXTRA_JSON = sys.argv[1:]

dirName = Path(SRCDIR).name

os.makedirs(cwd / "out/src", exist_ok=True)
os.makedirs(cwd / "out/javadoc" / dirName, exist_ok=True)

os.chdir(cwd / "out/src")
subprocess.run(["java", "-jar", EXTRA_JAVADOC_JAR, SRCDIR, EXTRA_JSON])
os.chdir(cwd / "out/javadoc" / dirName)

outDir = cwd / "out/src" / dirName
subprocess.run(["javadoc", "-sourcepath", outDir, "-subpackages", "."])