import os
import getpass
from pathlib import Path

def register_startup():
    user = getpass.getuser()
    startup_dir = f"C:/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
    current_script = os.path.abspath("main.py")
    dest = Path(startup_dir) / "LabShieldClient.bat"

    with open(dest, "w") as f:
        f.write(f'python "{current_script}"\n')

    print(f"✅ تم إضافة العميل للتشغيل التلقائي عند بدء النظام.")

if __name__ == "__main__":
    register_startup()
