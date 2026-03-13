import sys
import subprocess

try:
    from pypdf import PdfReader
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pypdf"])
    from pypdf import PdfReader

pdf_path = r"c:\Users\admin\Documents\kouhei\pckup-landing\Pckup 2025 Rebrand\Brand Strategy\Pckup Brand Strategy.pdf"
try:
    reader = PdfReader(pdf_path)
    text = "\n".join(page.extract_text() for page in reader.pages)

    with open("pdf_extracted_utf8.txt", "w", encoding="utf-8") as out:
        out.write(text)
    print("Done")
except Exception as e:
    print(f"Error reading PDF: {e}")
