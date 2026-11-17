from pathlib import Path

from PIL import Image

source_dir = Path("creo-originals")
output_dir = Path("images")

output_dir.mkdir(exist_ok=True)

for tif_file in source_dir.iterdir():
    if tif_file.suffix.lower() in (".tif", ".tiff"):
        with Image.open(tif_file) as img:
            output_name = tif_file.stem + ".png"
            output_path = output_dir / output_name

            img.convert("RGB").save(output_path, "PNG")

            print(f"Converted: {tif_file.name} -> {output_name}")

print("\nConversion complete!")
