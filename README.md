# Manga-Fixed-Unformatter
A very simple python script that undoes the Manga Fixed Format used by comixology on some manga.

Run the script/executable in the same folder as the image files. The script will take the double spreads and output single pages in the correct order in a subfolder called "out". It will also attempt to copy the cover page over and delete the split version, however the implementation is janky and may not work properly. Depending on the amount of pages, the final page may also end up broken, however I cannot be bothered to find a fix to this, so if this happens you'll have to copy it over manually and delete the broken version.
