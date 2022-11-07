def generate_desktop_entry(app_id):
    return f"""
[Desktop Entry]
Name=Notion Repackaged
Exec=notion-app.sh
Type=Application
Icon={app_id}
    """.strip()
