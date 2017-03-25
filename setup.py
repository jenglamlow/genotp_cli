# from distutils.core import setup
# import py2exe

# setup(console=[
#         {
#             "script": 'genotp.py',
#             "dest_base": "genotp"
#         }],
#     options={
#         "py2exe":
#         {
#             "bundle_files": 2,
#             "compressed": True,
#             "optimize": 1,
#             "packages": ['pyotp']
#         }
#     },
#     zipfile=None

# )

import sys
from cx_Freeze import setup, Executable

setup(
    name = "OTP Generation",
    version = "1.0",
    description = "Command Line Tool for TOPT Generation",
    executables = [Executable("genotp.py", base = "Win32GUI")])
