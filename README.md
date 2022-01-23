## NOTE ##
Due to recent changes in how Comixology works, this script is no longer needed to rip from there, Comixology purchases are now avalible through a Kindle library, allowing you to rip them in higher resolution than the previous chrome extension, and not in manga fixed format.

# Manga-Fixed-Unformatter
A somewhat simple python script that undoes the Manga Fixed Format used by comixology on some manga.

Run the script or executable either from the folder where you wish to split the manga, or
provide the `--directory` argument (short form `-d`) to point the script to the desired
folder to split the images in.

Works by checking the cover page and comparing the aspect ratio of the cover page to the last page
to prevent splitting (and potentially breaking) a single page at the end.

## Usage ##
Assuming the Python script is being used with the directory argument:
```bash
python MangaFixedUnformatter.py --directory /path/to/manga/volume
```
Assuming the python script is being called from the target directory:
```bash
python D:\Tools\MangaFixedUnformatter.py
```
Arguments and usage should be the same for the executable release version.

# Dependencies
1. Python >= 3.5 (Not needed for the executable version)
2. Image Magick
