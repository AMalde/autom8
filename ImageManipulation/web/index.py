from pathlib import Path
from PIL import Image

def optimize_images(source_folder, dest_folder, max_width=1920, quality=80, convert_to_webp=True):
    source = Path(source_folder)
    dest = Path(dest_folder)
    dest.mkdir(parents=True, exist_ok=True)

    for file in source.rglob("*"):
        if file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
            try:
                img = Image.open(file)
                img = img.convert("RGB")  # Ensure compatibility

                # Resize if too large
                if img.width > max_width:
                    new_height = int((max_width / img.width) * img.height)
                    img = img.resize((max_width, new_height), Image.ANTIALIAS)

                # Save
                new_name = file.stem + (".webp" if convert_to_webp else file.suffix.lower())
                new_path = dest / new_name
                img.save(new_path, format="WEBP" if convert_to_webp else img.format, quality=quality, optimize=True)

                print(f"✔ Optimized: {file.name} → {new_path.name}")

            except Exception as e:
                print(f"❌ Skipped {file.name}: {e}")