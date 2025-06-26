import fitz


def extract_text_from_pdf(path: str) -> str:
    """
    Extracts text from the given PDF file.
    """
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text
