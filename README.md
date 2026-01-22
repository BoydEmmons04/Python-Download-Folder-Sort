# Downloads Organizer (Python)

A simple Python script that organizes files in your `~/Downloads` folder by moving them into common folders in your home directory (`Documents`, `Music`, `Pictures`, `Videos`, `Code`) based on file extension.

It only scans the **top level** of `~/Downloads` (no subfolders), and it avoids overwriting files by appending ` (n)` to duplicates.

---

## What it does

- Scans: `~/Downloads`
- For each **regular file** in that folder:
  - Reads its extension (case-insensitive)
  - If the extension is recognized, moves the file to the matching destination folder:
    - `~/Documents`
    - `~/Music`
    - `~/Pictures`
    - `~/Videos`
    - `~/Code`
  - If the extension is missing or not in the map, it leaves the file in `Downloads`
- Prevents overwrites by renaming on collision:
  - `report.pdf` → `report (1).pdf`, `report (2).pdf`, etc.

At the end, it prints a summary like:

```text
Done. Moved X file(s). Skipped Y (folders, no/unknown extension).
