import os
from pathlib import Path
import subprocess
import argparse

parser = argparse.ArgumentParser(description="Split all combined manga pages \
                                 in a directory for easier reading!\n\
                                 Made by Cwavs & Riven",
                                 prog="Manga Fixed Unformatter")
parser.add_argument("--directory", "-d", dest="target", type=str,
                    default=str(Path.cwd()),
                    help="Specify the directory to take the images from.")
parser.add_argument("--debug", "-D", dest="debug", action="store_true",
                    help="Turn on the spammy debug output in an attempt to\
help us fix bugs and unbreak the script.")

def blind_copy(file: str, p_out: Path) -> None:
    """Blindly copy `file` to the output path with no processing.

    Opens both files in binary mode. If it's text, get rekt.
    """
    file = file.resolve()
    p_out = p_out.resolve()
    with open(file, "rb") as f:
        fout = Path(str(p_out)+"/"+os.path.basename(file))
        with open(fout, "wb") as f2:
            f2.write(f.read())

def truncate_path(target: Path) -> None:
    """Truncate a path to ensure it's completely empty

    Honestly I should make this a PyPI module.
    """
    for f in target.glob("*"):
        if f.is_file():
            # Simulate `rm -f f`
            f.unlink(missing_ok=True)
        else:
            # This file is a folder, truncate it first
            truncate_path(f)
            # Then `rm -rf f`
            f.rmdir()

args = parser.parse_args()
print("Manga Fixed Unformatter V1.0")
print("Written by Cwavs, with lots of pain (fuck you image magick docs).\
\nSmall fixes made by Riven, with lots of love.")
if args.debug: print("Debugging output turned on! Expect spammy behavior!")
target = Path(args.target).resolve()
if args.debug: print(f"Currently looking in {Path.cwd()}.")
if not target.exists():
    print("Provided directory does not exist. Try again.")
    # Exit and notify the system there was an error.
    # This is good for automation purposes
    exit(1)
out_path = Path(str(target)+"/out").resolve()
# Make sure the out path exists
out_path.mkdir(parents=True, exist_ok=True)
truncate_path(out_path)
files = sorted(target.glob("*.png"))
# Grab the cover page width and height
width, height = subprocess.run(["magick", "identify", "-format", "%w;%h", files[0]], stdout=subprocess.PIPE).stdout.decode('utf-8').split(";")
lwidth, lheight = width, height = subprocess.run(["magick", "identify", "-format", "%w;%h", files[-1]], stdout=subprocess.PIPE).stdout.decode('utf-8').split(";")
if args.debug:
    print(f"Cover sizes (wxh): {width}x{height}. AR {int(width)/int(height)}")
    print(f"Last page sizes (wxh): {lwidth}x{lheight}. AR {int(lwidth)/int(lheight)}")
blind_copy(files[0], out_path)
files = files[1:]
if int(width)/int(height) == int(lwidth)/int(lheight):
    if args.debug: print("Blindly copying final page...")
    blind_copy(files[-1], out_path)
    files = files[:-1]
print("Splitting Pages...")
# Set those as the max sizes for every page, this also "crops" the cover to its own sizes
for f in files:
    if args.debug: print(f)
    subprocess.run(["magick", "mogrify", "-path", str(out_path), "-crop", f"50%x100%", "-reverse", "-quality", "100", f])
print("Done!")
