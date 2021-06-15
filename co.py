import subprocess
import os, shutil

def conv(files):
    for d in files:
        subprocess.run(["libwebp/bin/cwebp", "src/" + d, "-quiet", "-o", "out/" + d.split(".")[0] + ".webp"])
        os.remove("src/" + d)

dirs = os.listdir("src")

if not os.path.exists("out"):
    os.mkdir("out")

conv(dirs)

print("done")

