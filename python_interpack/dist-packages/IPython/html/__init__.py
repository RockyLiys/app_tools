"""The IPython HTML Notebook"""

import os
# Packagers: modify this line if you store the notebook static files elsewhere
if os.path.exists("/usr/share/ipython/notebook/static"):
    DEFAULT_STATIC_FILES_PATH = "/usr/share/ipython/notebook/static"
else:
    DEFAULT_STATIC_FILES_PATH = os.path.join(os.path.dirname(__file__), "static")

del os

from .nbextensions import install_nbextension
