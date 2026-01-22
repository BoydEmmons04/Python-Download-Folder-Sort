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

## File Type Rules

Extentions are mapped using 'EXT_MAP'.
Below is a high-level summary of what goes where.

- **Documents**
    - pdf, doc, docx, rtf, txt, md
    - ppt, pptx, xls, xlsx
    - csv, tsv, json, xml, yml, yaml, epub

- **Music / Audio**
    - mp3, m4a, aac, wav, flac, ogg, opus

- **Images**
    - jpg, jpeg, png, gif, webp, bmp
    - tif, tiff, svg, heic, heif

- **Videos**
    - mp4, m4v, mov, mkv, avi, wmv, webm

- **Code**
    - py, ipynb, js, ts, java, c, cp, h, cs, go, rs, swift
    - sh, bash, ps1, sql, html, css, toml, ini, cfg, conf, cmake, gradle, mk

## Requirements

- Python: 3.x (3.8+ Recommended)
- Dependencies: None (standard library only)

## Setup

- 1) Navigate to the directory containing the script

**macOS / Linux**
- 2)
'''bash
git push
