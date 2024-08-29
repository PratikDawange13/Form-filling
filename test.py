import fitz
import PyPDF2
import docx

#def extract_text_from_pdf(pdf_file):
 #   with pymupdf.open(pdf_file) as doc:
 #       text = ""
  #      for page in doc:
 #           text += page.get_text("text")  # Extract text from each page
 #       return text
def extract_text_from_pdf(pdf_bytes):
    with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text("text") # Extract text from each page
        return text



# def extract_text_from_pdf(pdf_path):
#     with open(pdf_path, 'rb') as file:
#         reader = PyPDF2.PdfReader(file)
#         text = ""
#         for page in reader.pages:
#             text += page.extract_text()
#     return text


def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return " ".join([paragraph.text for paragraph in doc.paragraphs])