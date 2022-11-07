#! /bin/python3

# IMPORTS

import json
import os
import shutil

from cli import parse_args
from constants import (APP_NAME, FLATPAK_APP_ID, LOGO_FILETYPE, LOGO_NAME, LOGO_SIZE,
                       NOTION_REPACKAGED_ZIP_MD5, NOTION_REPACKAGED_ZIP_URL)
from desktop_entry import generate_desktop_entry
from directory import (ASSETS_DIR, BUILD_DIR, DESKTOP_ENTRY_DIR, OUT_DIR,
                       prepare_build_directory)
from flatpak_build import generate_flatpak_build_config

# CLI
args = parse_args()
do_install = args.install

# Setup
prepare_build_directory()

# Flatpak Build Config

config = generate_flatpak_build_config(
    app_id=FLATPAK_APP_ID,
    notion_repackaged_zip_url=NOTION_REPACKAGED_ZIP_URL,
    notion_repackaged_zip_md5=NOTION_REPACKAGED_ZIP_MD5,
    build_dir=BUILD_DIR,
    logo_path=LOGO_NAME,
    logo_size=LOGO_SIZE,
    logo_filetype=LOGO_FILETYPE,
)
json_output = json.dumps(config, indent=4)
with open(f"{BUILD_DIR}/{FLATPAK_APP_ID}.json", "w") as f:
    f.write(json_output)

# Desktop Entry
with open(f"{DESKTOP_ENTRY_DIR}/{FLATPAK_APP_ID}.desktop", "w") as f:
    f.write(generate_desktop_entry(app_id=FLATPAK_APP_ID, app_name=APP_NAME))
shutil.copyfile(f"{ASSETS_DIR}/{LOGO_NAME}",
                f"{DESKTOP_ENTRY_DIR}/{LOGO_NAME}")

# Run flatpak builder
if do_install:
    os.system(
        f"flatpak-builder --user --install --force-clean  {OUT_DIR} {BUILD_DIR}/{FLATPAK_APP_ID}.json")
else:
    os.system(
        f"flatpak-builder {OUT_DIR} {BUILD_DIR}/{FLATPAK_APP_ID}.json")
