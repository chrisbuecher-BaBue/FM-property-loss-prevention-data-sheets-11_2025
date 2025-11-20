import fitz  # PyMuPDF
import os

PDF_DIR = "pdfs"
TEXT_DIR = "pdf_texts"
os.makedirs(TEXT_DIR, exist_ok=True)

for filename in os.listdir(PDF_DIR):
    if filename.lower().endswith(".pdf"):
        path = os.path.join(PDF_DIR, filename)
        doc = fitz.open(path)
        text = "\n".join(page.get_text() for page in doc)
        out_path = os.path.join(TEXT_DIR, filename + ".txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"✅ Text extrahiert: {filename}")
