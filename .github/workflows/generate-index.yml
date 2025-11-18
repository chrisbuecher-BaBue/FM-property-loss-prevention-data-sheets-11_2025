# generate_index.py

import os

REPO_URL = "https://raw.githubusercontent.com/chrisbuecher-BaBue/FM-property-loss-prevention-data-sheets-11_2025/main"
PDF_DIR = "."
OUTPUT_FILE = "index.md"

pdf_files = [f for f in sorted(os.listdir(PDF_DIR)) if f.lower().endswith(".pdf")]
if not pdf_files:
    print("Keine PDF-Dateien im Hauptverzeichnis gefunden. Index wird nicht erstellt.")
    exit(0)

lines = ["# 📄 PDF-Index\n", "\nHier sind alle verfügbaren PDF-Dateien:\n"]
for filename in pdf_files:
    raw_url = f"{REPO_URL}/{filename}"
    lines.append(f"- [{filename}]({raw_url})\n")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.writelines(lines)
