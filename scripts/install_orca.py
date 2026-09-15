#!/usr/bin/env python3
import json
import os
import shutil
import subprocess
import sys
import uuid
from pathlib import Path

def is_orca_running():
    try:
        output = subprocess.check_output(["pgrep", "-x", "Orca"], text=True).strip()
        return len(output) > 0
    except subprocess.CalledProcessError:
        return False

def install_orca():
    repo_root = Path(__file__).resolve().parent.parent
    dist_dir = repo_root / "dist"
    pet_json_path = dist_dir / "pet.json"
    spritesheet_path = dist_dir / "spritesheet.webp"

    if not pet_json_path.exists() or not spritesheet_path.exists():
        print(f"❌ Assets not found in {dist_dir}. Run build first.")
        sys.exit(1)

    orca_user_data = Path.home() / "Library/Application Support/orca"
    profile_data_file = orca_user_data / "profiles/local-default/orca-data.json"

    if not orca_user_data.exists():
        print(f"❌ Orca directory not found at {orca_user_data}")
        sys.exit(1)

    if is_orca_running():
        print("⚠️  Orca IDE сейчас запущена.")
        print("   Чтобы изменения в конфигурации сохранились, закройте Orca (Cmd+Q) и запустите этот скрипт снова,")
        print("   ЛИБО используйте встроенную функцию меню Orca:")
        print("   Кликните на 'Pet' в строке состояния -> 'Choose pet' -> 'Import .codex-pet bundle...'")
        print(f"   и выберите папку: {dist_dir / 'avari.codex-pet'}")
        sys.exit(1)

    pet_uuid = str(uuid.uuid4())
    custom_pet_dir = orca_user_data / "sidekicks/custom" / pet_uuid
    custom_pet_dir.mkdir(parents=True, exist_ok=True)

    shutil.copy(pet_json_path, custom_pet_dir / "pet.json")
    shutil.copy(spritesheet_path, custom_pet_dir / "spritesheet.webp")

    print(f"📁 Файлы скопированы в: {custom_pet_dir}")

    if profile_data_file.exists():
        with open(profile_data_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        ui = data.setdefault("ui", {})
        status_bar = ui.setdefault("statusBarItems", [])
        if "pets" not in status_bar:
            status_bar.append("pets")

        ui["petVisible"] = True
        ui["petId"] = pet_uuid
        ui["statusBarVisible"] = True

        custom_pets = ui.setdefault("customPets", [])
        # Remove any previous avari entry
        custom_pets = [p for p in custom_pets if p.get("label") != "Авари" and p.get("id") != "avari"]

        custom_entry = {
            "id": pet_uuid,
            "label": "Авари",
            "fileName": "spritesheet.webp",
            "mimeType": "image/webp",
            "kind": "bundle",
            "sprite": {
                "frameWidth": 192,
                "frameHeight": 208,
                "columns": 8,
                "rows": 11,
                "sheetWidth": 1536,
                "sheetHeight": 2288,
                "fps": 8,
                "defaultAnimation": "idle",
                "animations": {
                    "idle": {"row": 0, "frames": 6, "frameDurationsMs": [1680, 660, 660, 840, 840, 1920]},
                    "running-right": {"row": 1, "frames": 8, "frameDurationsMs": [120, 120, 120, 120, 120, 120, 120, 220]},
                    "running-left": {"row": 2, "frames": 8, "frameDurationsMs": [120, 120, 120, 120, 120, 120, 120, 220]},
                    "waving": {"row": 3, "frames": 4, "frameDurationsMs": [140, 140, 140, 280]},
                    "jumping": {"row": 4, "frames": 5, "frameDurationsMs": [140, 140, 140, 140, 280]},
                    "failed": {"row": 5, "frames": 8, "frameDurationsMs": [140, 140, 140, 140, 140, 140, 140, 240]},
                    "waiting": {"row": 6, "frames": 6, "frameDurationsMs": [150, 150, 150, 150, 150, 260]},
                    "running": {"row": 7, "frames": 6, "frameDurationsMs": [120, 120, 120, 120, 120, 220]},
                    "review": {"row": 8, "frames": 6, "frameDurationsMs": [150, 150, 150, 150, 150, 280]}
                }
            }
        }
        custom_pets.append(custom_entry)
        ui["customPets"] = custom_pets

        with open(profile_data_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"✨ Авари успешно прописана в настройках Orca: {profile_data_file}")
        print("🚀 Теперь можно запускать Orca IDE!")
    else:
        print(f"⚠️ Файл профиля не найден: {profile_data_file}")

if __name__ == "__main__":
    install_orca()
