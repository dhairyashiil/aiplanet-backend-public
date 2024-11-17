import fitz  # PyMuPDF
from io import BytesIO

def extract_text_from_pdf(pdf_file: BytesIO) -> str:
    """Extract text from a PDF file using PyMuPDF."""
    try:
        # Open the PDF from the in-memory file (no need to pass filename)
        doc = fitz.open(stream=pdf_file, filetype="pdf")
        text = ""
        
        # Iterate through all the pages in the PDF
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)  # Load each page
            text += page.get_text()  # Extract text from the page
        
        return text
    except Exception as e:
        raise Exception(f"Error extracting text from PDF: {str(e)}")
