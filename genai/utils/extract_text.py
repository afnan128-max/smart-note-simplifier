import fitz  # PyMuPDF
import io

def extract_text_from_pdf(file):
    if file.name.endswith('.txt'):
        return file.read().decode("utf-8")
    
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text
