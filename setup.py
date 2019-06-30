import glob
import os
import sys

os.environ['TCL_LIBRARY'] = r'C:\Users\User\AppData\Local\Programs\Python\Python37\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\User\AppData\Local\Programs\Python\Python37\tcl\tk8.6'

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"
executables = [
    Executable("fileWindows.py", base=base)
]

# VARREDURA NOS DIRETÓRIOS { DIRPNG , DIRWAV }
allArqDir = []
for diretirio in ["DirPNG", "DirWAV"]:
    for f in glob.glob(f"{diretirio}\*"):
        if len(f.split(".")) == 2:
            allArqDir.append(f)
        else:
            for f1 in glob.glob(f'{f}\*'):
                allArqDir.append(f1)

buildOptions = dict(
    packages=["tkinter"],
    includes=["winsound", "operator", "fileClass", "functools", "tkinter.font"],
    include_files=allArqDir,
    excludes=[]
)
allArqDir.append(r"C:\Users\User\AppData\Local\Programs\Python\Python37\DLLs\tcl86t.dll")
allArqDir.append(r"C:\Users\User\AppData\Local\Programs\Python\Python37\DLLs\tk86t.dll")
setup(
    name="ProjectBloodBladeSociety",
    version="BETA",
    options=dict(build_exe=buildOptions),
    executables=executables, requires=['cx_Freeze']
)
