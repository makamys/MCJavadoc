import subprocess
import sys
import os
from pathlib import Path

JAVADOC = Path(os.environ['JAVA_HOME']) / "bin" / "javadoc" if os.environ['JAVA_HOME'] else "javadoc"

if len(sys.argv) != 4:
    sys.exit("Usage: {} EXTRA_JAVADOC_JAR SRCDIR EXTRA_JSON".format(sys.argv[0]))

cwd = Path(os.getcwd())

EXTRA_JAVADOC_JAR, SRCDIR, EXTRA_JSON = sys.argv[1:]

dirName = Path(SRCDIR).name
outJavadocDir = os.path.splitext(cwd / "docs" / Path(EXTRA_JSON).name)[0]
outSrcDir = cwd / "build/src"

os.makedirs(outSrcDir, exist_ok=True)
os.makedirs(outJavadocDir, exist_ok=True)

os.chdir(outSrcDir)
subprocess.run(["java", "-jar", EXTRA_JAVADOC_JAR, SRCDIR, EXTRA_JSON]).check_returncode()
os.chdir(outJavadocDir)

subprocess.run([JAVADOC, "-sourcepath", outSrcDir / dirName, "-subpackages", "net:cpw:ibxm:paulscode"])
