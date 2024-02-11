import os
import pathlib
from pathlib import Path
pathlib.PosixPath = pathlib.WindowsPath

os.system("python detect.py --weights best.pt --img 545 --conf 0.5 --source 0")
