import fitz  # PyMuPDF
import sys

def compress_pdf(input_path: str, output_path: str):
    doc = fitz.open(input_path)
    doc.save(
        output_path,
        garbage=4,        # remove unused objects
        deflate=True,     # compress streams
        clean=True        # clean up content streams
    )
    doc.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python CompressPDF.py <input_pdf> <output_pdf>")
        print("Example: python CompressPDF.py document.pdf document_compressed.pdf")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
        compress_pdf(input_file, output_file)
        print(f"✅ PDF compressed successfully!")
        print(f"Input: {input_file}")
        print(f"Output: {output_file}")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)