import os
from pathlib import Path
import subprocess

print("Manga Fixed Unformatter V1.0")
print("Written by Cwavs, with lots of pain (fuck you image magick docs).\
       Small fixes made by Riven, with lots of love.")
# Account for users being idiots
print(f"Currently looking in {Path.cwd()}. Is this correct?")
target = input("Provide path or press enter > ") or Path.cwd()
# Make sure the path is absolute
target = Path(str(target)).resolve()
if not target.exists():
    print("Provided directory does not exist. Try again.")
    # Exit and notify the system there was an error.
    # This is good for automation purposes
    exit(1)
out_path = Path(str(target)+"/out").resolve()
# Make sure the out path exists
out_path.mkdir(parents=True, exist_ok=True)
files = sorted(target.glob("*.png"))
# Grab the cover page width and height
width, height = subprocess.run(["magick", "identify", "-format", "%w;%h", files[0]], stdout=subprocess.PIPE).stdout.decode('utf-8').split(";")

print("Splitting Pages...")
# Set those as the max sizes for every page, this also "crops" the cover to its own sizes
for f in files:
    subprocess.run(["magick", "mogrify", "-path", str(out_path), "-crop", f"{width}x{height}!", "-reverse", "-quality", "100", f])
print("Done!")
