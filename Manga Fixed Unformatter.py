import os
import subprocess
import shutil

print("Manga Fixed Unformatter V1.0")
print("Written by Cwavs, with lots of pain (fuck you image magick docs)")
try:
    os.mkdir("out")
except:
    shutil.rmtree("out")
    os.mkdir("out")
print("Splitting Pages...")
subprocess.call("magick mogrify -path out -crop 50%x100% -reverse -quality 100 *.png", shell=True)
shutil.copy("page000.png", "out")
os.system("cd out")
os.remove("page000-0.png")
os.remove("page000-1.png")
print("Done!")
