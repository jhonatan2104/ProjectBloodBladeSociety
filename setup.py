import os
import sys

os.environ['TCL_LIBRARY'] = r'C:\Users\User\AppData\Local\Programs\Python\Python37\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\User\AppData\Local\Programs\Python\Python37\tcl\tk8.6'

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"
executables = [
    Executable("fileMain.py", base=base)
]

allArqDir = ["DirPNG", "DirWAV", "TutorialTEXT.txt",
             r"C:\Users\User\AppData\Local\Programs\Python\Python37\DLLs\tcl86t.dll",
             r"C:\Users\User\AppData\Local\Programs\Python\Python37\DLLs\tk86t.dll"]

buildOptions = dict(
    packages=["tkinter"],
    includes=["winsound", "operator", "fileClass", "functools", "tkinter.font", "fileWindows", "tkinter.scrolledtext"],
    include_files=allArqDir,
    excludes=[]
)
setup(
    name="ProjectBloodBladeSociety",
    version="BETA",
    options=dict(build_exe=buildOptions),
    executables=executables, requires=['cx_Freeze']
)
