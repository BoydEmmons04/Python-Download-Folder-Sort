#!/usr/bin/env python3
from pathlib import Path
import shutil

HOME = Path.home()
DOWNLOADS = HOME / "Downloads"

# Destination folders
DESTS = {
    "documents": HOME / "Documents",
    "music":     HOME / "Music",
    "pictures":  HOME / "Pictures",
    "videos":    HOME / "Videos",
    "code":      HOME / "Code",
}

# Map extensions -> destination key (no leading dots, lowercase)
EXT_MAP = {
    # Documents
    "pdf":"documents","doc":"documents","docx":"documents","rtf":"documents","txt":"documents",
    "md":"documents","odt":"documents","ppt":"documents","pptx":"documents","key":"documents",
    "xls":"documents","xlsx":"documents","csv":"documents","tsv":"documents","json":"documents",
    "xml":"documents","yml":"documents","yaml":"documents","epub":"documents",

    # Music / Audio
    "mp3":"music","m4a":"music","aac":"music","wav":"music","flac":"music","ogg":"music","oga":"music","opus":"music",

    # Pictures / Images
    "jpg":"pictures","jpeg":"pictures","png":"pictures","gif":"pictures","webp":"pictures",
    "bmp":"pictures","tif":"pictures","tiff":"pictures","svg":"pictures","heic":"pictures","heif":"pictures",

    # Videos
    "mp4":"videos","m4v":"videos","mov":"videos","mkv":"videos","avi":"videos","wmv":"videos","webm":"videos",

    # Code / Dev
    "py":"code","ipynb":"code","js":"code","ts":"code","jsx":"code","tsx":"code",
    "java":"code","c":"code","h":"code","hpp":"code","hh":"code","cpp":"code","cc":"code",
    "cs":"code","go":"code","rs":"code","swift":"code","kt":"code","kts":"code",
    "php":"code","rb":"code","sh":"code","bash":"code","ps1":"code","sql":"code",
    "html":"code","css":"code","scss":"code","sass":"code","ini":"code",".env":"code",".env.local":"code",
    "toml":"code","cfg":"code","conf":"code","gradle":"code","cmake":"code","makefile":"code","mk":"code",
}

def safe_move(src: Path, dest_dir: Path) -> Path:
    """Move src into dest_dir, avoiding overwrite by adding (n)."""
    dest_dir.mkdir(parents=True, exist_ok=True)
    target = dest_dir / src.name
    if not target.exists():
        shutil.move(str(src), str(target))
        return target

    stem, suffix = src.stem, src.suffix
    i = 1
    while True:
        candidate = dest_dir / f"{stem} ({i}){suffix}"
        if not candidate.exists():
            shutil.move(str(src), str(candidate))
            return candidate
        i += 1

def main():
    if not DOWNLOADS.exists():
        print(f"Downloads folder not found: {DOWNLOADS}")
        return

    moved = 0
    skipped = 0

    for entry in DOWNLOADS.iterdir():
        # Only handle regular files in the top level
        if not entry.is_file():
            continue

        ext = entry.suffix.lower().lstrip(".")
        if not ext:
            skipped += 1
            continue

        dest_key = EXT_MAP.get(ext)
        if not dest_key:
            # Not in our map; leave it in Downloads
            skipped += 1
            continue

        dest_dir = DESTS[dest_key]
        safe_move(entry, dest_dir)
        moved += 1

    print(f"Done. Moved {moved} file(s). Skipped {skipped} (folders, no/unknown extension).")

if __name__ == "__main__":
    main()

