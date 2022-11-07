#! /bin/python3

# IMPORTS

import os
from pathlib import Path
import zipfile
import shutil
import subprocess

# CONSTANTS

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
BUILD_DIR = CURRENT_DIR+"/build"
SOURCE_DIR = BUILD_DIR+"/source"
OUT_DIR = BUILD_DIR+"/out"

# CONFIG

NOTION_REPACKAGED_ZIP = CURRENT_DIR+"/notion-app-2.0.18-1.zip"
FLATPAK_APP_ID = "org.haryp.NotionRepackaged"


# SETUP

if Path(BUILD_DIR).exists():
    shutil.rmtree(Path(BUILD_DIR))
Path(BUILD_DIR).mkdir()

Path(OUT_DIR).mkdir()


# Generate yaml

yaml = f"""
app-id: {FLATPAK_APP_ID}
runtime: org.freedesktop.Platform
runtime-version: '21.08'
sdk: org.freedesktop.Sdk
base: org.electronjs.Electron2.BaseApp
base-version: '21.08'
command: notion-app.sh
modules:
  - name: notion-app
    buildsystem: simple
    build-commands:
      - mkdir -p /app/bin/
      - cp -r ./* /app
      - echo "/app/notion-app --no-sandbox" > /app/bin/notion-app.sh
      - ls /app/bin/
      - chmod +x /app/bin/notion-app.sh
    sources:
      - type: archive
        path: "{NOTION_REPACKAGED_ZIP}"
        strip-components: 0

finish-args:
  - --share=ipc
  - --socket=x11
  - --socket=pulseaudio
  - --share=network
"""
with open(f"{BUILD_DIR}/{FLATPAK_APP_ID}.yaml", "w") as f:
    f.write(yaml)



# Run flatpak builder

os.system(f"flatpak-builder --user --install --force-clean  {OUT_DIR} {BUILD_DIR}/{FLATPAK_APP_ID}.yaml")

# Start Application
#os.system(f"flatpak run {FLATPAK_APP_ID}")