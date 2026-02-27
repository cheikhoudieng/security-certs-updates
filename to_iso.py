import pycdlib
import os

SOURCE_DIR = "BUILD_ISO"
ISO_NAME = "setup.iso"

iso = pycdlib.PyCdlib()
iso.new(interchange_level=3)

created_dirs = set()

for root, dirs, files in os.walk(SOURCE_DIR):
    # chemin relatif depuis BUILD_ISO
    rel_path = os.path.relpath(root, SOURCE_DIR)

    if rel_path != ".":
        iso_dir = "/" + rel_path.replace("\\", "/").upper()

        if iso_dir not in created_dirs:
            iso.add_directory(iso_dir)
            created_dirs.add(iso_dir)

    for file in files:
        full_path = os.path.join(root, file)

        iso_file_path = "/" + os.path.relpath(full_path, SOURCE_DIR)
        iso_file_path = iso_file_path.replace("\\", "/").upper() + ";1"

        iso.add_file(full_path, iso_file_path)

iso.write(ISO_NAME)
iso.close()

print(f"[+] ISO créé avec succès : {ISO_NAME}")
