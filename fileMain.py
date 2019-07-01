from fileWindows import *
from fileClass import *
import sys
'''if sys.platform == "win32":
   TelaInicio().construtor()'''
root = Tk()
root.geometry("300x300")

root.bind("<a>",lambda event: print("A precionado"))

root.mainloop()