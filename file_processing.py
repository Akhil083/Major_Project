from pymupdf import fitz  # PyMuPDF
from docx import Document

def display_pdf(file_path):
    """
    Function to display the PDF content in its original format.
    :param file_path: The path to the PDF file.
    :return: A list of strings, where each string represents the content of a page.
    """
    pdf_content = []
    with fitz.open(file_path) as pdf:
        for page_num in range(pdf.page_count):
            page = pdf.load_page(page_num)
            pdf_content.append(page.get_text())
    return pdf_content

def extract_text_chunks(file_path, chunk_size=1000):
    """
    Function to extract text from the file in chunks while retaining DOCX formatting.
    Supports both PDF and DOCX files.
    :param file_path: The path to the file (PDF or DOCX).
    :param chunk_size: The size of each text chunk (default: 1000 characters).
    :return: A list of text chunks extracted from the file.
    """
    text_chunks = []

    if file_path.lower().endswith('.pdf'):
        # Extract text from PDF
        with fitz.open(file_path) as pdf:
            full_text = ""
            for page_num in range(pdf.page_count):
                page = pdf.load_page(page_num)
                full_text += page.get_text()

            # Split the text into chunks
            text_chunks = [full_text[i:i + chunk_size] for i in range(0, len(full_text), chunk_size)]

    elif file_path.lower().endswith('.docx'):
        # Extract text from DOCX
        doc = Document(file_path)
        full_text = ""
        for paragraph in doc.paragraphs:
            full_text += paragraph.text + "\n"

        # Split the text into chunks while maintaining DOCX formatting
        text_chunks = [full_text[i:i + chunk_size] for i in range(0, len(full_text), chunk_size)]

    else:
        raise ValueError("Unsupported file format. Please upload a PDF or DOCX file.")

    return text_chunks
