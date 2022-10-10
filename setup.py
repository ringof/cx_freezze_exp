import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["PyQt5"]}

base = None

setup(
  name="V-TOOLS",
  version="0.1 ALPHA",
  description="V-TOOLS",
  options={"build_exe": build_exe_options},
  executables=[Executable('qt_folder_popup.py', base=base, icon='hat.ico')]
)
