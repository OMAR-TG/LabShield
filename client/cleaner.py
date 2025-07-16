import os
import shutil
from pathlib import Path
import getpass

def clear_user_files():
    user = getpass.getuser()
    folders = [
        f"C:/Users/{user}/Desktop",
        f"C:/Users/{user}/Documents",
        f"C:/Users/{user}/Downloads",
        f"D:/Downloads",
    ]

    for folder in folders:
        path = Path(folder)
        if path.exists():
            for item in path.iterdir():
                try:
                    if item.is_file():
                        item.unlink()
                    elif item.is_dir():
                        shutil.rmtree(item)
                except Exception as e:
                    print(f"❌ فشل في حذف: {item} بسبب {e}")
