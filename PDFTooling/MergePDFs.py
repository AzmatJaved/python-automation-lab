import fitz  # PyMuPDF

def merge_pdfs(input_paths: list[str], output_path: str):
    merged = fitz.open()
    for path in input_paths:
        doc = fitz.open(path)
        merged.insert_pdf(doc)
        doc.close()
    merged.save(output_path)
    merged.close()