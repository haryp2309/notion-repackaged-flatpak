#! /bin/python3

# IMPORTS

import os
import shutil
import subprocess
from pathlib import Path

# CONSTANTS

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
BUILD_DIR = CURRENT_DIR+"/build"
OUT_DIR = BUILD_DIR+"/out"

# CONFIG

FLATPAK_APP_ID = "org.haryp.NotionRepackaged"
NOTION_REPACKAGED_ZIP_URL = "https://github.com/notion-enhancer/notion-repackaged/releases/download/v2.0.18-1/notion-app-2.0.18-1.zip"
NOTION_REPACKAGED_ZIP_MD5 = "235f3c20c3c27a63d172b6cbf15c9571"


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
      - chmod +x /app/bin/notion-app.sh
    sources:
      - type: archive
        url: "{NOTION_REPACKAGED_ZIP_URL}"
        md5: "{NOTION_REPACKAGED_ZIP_MD5}"
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

os.system(
    f"flatpak-builder --user --install --force-clean  {OUT_DIR} {BUILD_DIR}/{FLATPAK_APP_ID}.yaml")

# Start Application
#os.system(f"flatpak run {FLATPAK_APP_ID}")
