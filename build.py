from pathlib import Path
import subprocess
import shutil
import os

extraJavadocJar = Path("build") / "ExtraJavadoc" / "build" / "libs" / "ExtraJavadoc-0.0.jar"

if not extraJavadocJar.exists():
    subprocess.run(["git", "clone", "https://github.com/makamys/ExtraJavadoc", "build/ExtraJavadoc"])
    subprocess.run(["git", "checkout", "01ab63bedd5b923cceffb5764facf6b1478ced48"], cwd="build/ExtraJavadoc")
    subprocess.run("./gradlew build", cwd="build/ExtraJavadoc", shell=True)
    
    assert extraJavadocJar.exists()


mc7Sources = Path("mod") / "forge-1.7.10-10.13.4.1614" / "build" / "rfg" / "minecraft-src"

if not mc7Sources.exists():
    subprocess.run("./gradlew build", cwd="mod/forge-1.7.10-10.13.4.1614", shell=True)

os.makedirs("docs", exist_ok=True)
subprocess.run(["pandoc", "src/index.md", "-f", "markdown", "-t", "html", "-s", "-c", "style.css", "-o", "docs/index.html"])
shutil.copy("src/style.css", "docs/style.css")

subprocess.run([
    "python3",
    "build_docs.py",
    Path("build/ExtraJavadoc/build/libs/ExtraJavadoc-0.0.jar").absolute(),
    Path("mod/forge-1.7.10-10.13.4.1614/build/rfg/minecraft-src/java").absolute(),
    Path("extra/forge-1.7.10-10.13.4.1614.hjson").absolute()
])
