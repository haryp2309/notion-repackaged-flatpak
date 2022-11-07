def generate_desktop_entry(app_id, app_name):
    return f"""
[Desktop Entry]
Name={app_name}
Exec=notion-app.sh
Type=Application
Icon={app_id}
    """.strip()
