def generate_flatpak_build_config(
    app_id,
    notion_repackaged_zip_url,
    notion_repackaged_zip_md5,
    build_dir,
    logo_path,
    logo_size,
    logo_filetype
):
    return {
        "app-id": app_id,
        "runtime": "org.freedesktop.Platform",
        "runtime-version": "21.08",
        "sdk": "org.freedesktop.Sdk",
        "base": "org.electronjs.Electron2.BaseApp",
        "base-version": "21.08",
        "command": "notion-app.sh",
        "modules": [
            {
                "name": "notion-app",
                "buildsystem": "simple",
                "build-commands":  [
                    "mkdir -p /app/bin/",
                    "cp -r ./* /app",
                    "echo \"/app/notion-app --no-sandbox\" > /app/bin/notion-app.sh",
                    "chmod +x /app/bin/notion-app.sh",
                    "mkdir -p /app/share/applications/",
                    f"cp {app_id}.desktop /app/share/applications/",
                    f"mkdir -p /app/share/icons/hicolor/{logo_size}x{logo_size}/apps/",
                    f"cp {logo_path} /app/share/icons/hicolor/{logo_size}x{logo_size}/apps/{app_id}.{logo_filetype}",
                ],
                "sources": [
                    {
                        "type": "archive",
                        "url": notion_repackaged_zip_url,
                        "md5": notion_repackaged_zip_md5,
                        "strip-components": 0,
                    }, {
                        "type": "dir",
                        "path": build_dir + "/desktop-entry",
                    }
                ]
            }
        ],
        "finish-args": [
            "--share=ipc",
            "--socket=x11",
            "--socket=pulseaudio",
            "--share=network",
        ]
    }
