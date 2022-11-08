import os
import shutil
from pathlib import Path

SOURCE_DIR = os.path.dirname(os.path.realpath(__file__))
BUILD_DIR = SOURCE_DIR+"/../build"
OUT_DIR = BUILD_DIR+"/out"
DESKTOP_ENTRY_DIR = BUILD_DIR+"/desktop-entry"
ASSETS_DIR = SOURCE_DIR+"/assets"
REPO_DIR = BUILD_DIR+"/repo"


def prepare_build_directory():
    if Path(BUILD_DIR).exists():
        shutil.rmtree(Path(BUILD_DIR))
    Path(BUILD_DIR).mkdir()
    Path(OUT_DIR).mkdir()
    Path(DESKTOP_ENTRY_DIR).mkdir()
