import streamlit as st
import google.generativeai as genai
import PyPDF2
import unicodedata
import os
from markdown_pdf import MarkdownPdf, Section
import docx
import fitz
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("api_key")    
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# def extract_text_from_pdf(pdf_file):
#     pdf_path = pdf_file
#     with open(pdf_path, 'rb') as file:
#         reader = PyPDF2.PdfReader(file)
#         text = ""
#         for page in reader.pages:
#             text += page.extract_text()
#     return text

def extract_text_from_pdf(pdf_file):
    pdf_bytes = pdf_file.read()
    with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text("text") # Extract text from each page
        return text


def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return " ".join([paragraph.text for paragraph in doc.paragraphs])

def check_extrension(file_name):
    if file_name.lower().endswith(".pdf") :
        return "pdf"
    else:
        return "docx"

# Function to convert text to be latin-1 compatible
def convert_to_latin1_compatible(text):
    # Replace the en-dash with a hyphen
    text = text.replace('\u2013', '-')
    text = text.replace('\u2019', '-')
    text = text.replace('\u201c', '-')
    
    
    # Normalize and encode to latin-1, ignoring unsupported characters
    text = unicodedata.normalize('NFKD', text).encode('latin-1', 'ignore').decode('latin-1')
    
    return text


# streamlit app

st.title('Visa Form Filling')
st.header('Upload Questionnaire and Form')

form = st.file_uploader(label="Please Upload Form", type=["pdf","docx"])
questionnaries = st.file_uploader(label="Please Upload Questionnaries", type=["pdf","docx"])

if form and questionnaries:
    form_extension = check_extrension(form.name)
    questionnaries_extension = check_extrension(questionnaries.name)

    form_text = extract_text_from_pdf(form) if form_extension == "pdf" else extract_text_from_docx(form)
    questionnaries_text = extract_text_from_pdf(questionnaries) if questionnaries_extension == "pdf" else extract_text_from_docx(questionnaries)

    button = st.button("Generate Filled Form")

    if button:
        prompt1 = """Please go through all the information provided below for a person"""
        prompt2 = """Fill out the following form using the provided client information. Leave fields blank if the information is not availableUse, proper line breaks and markdown formatting in response. After completing the form, list all missing information under the heading "MISSING INFORMATION". Use proper line breaks and markdown formatting in response """
        
        # Generate content using the Generative Model
        response = model.generate_content([prompt1, questionnaries_text, prompt2, form_text])

        # Resolve the response
        response.resolve()
        filled_details = response.text

        # Convert to latin-1 compatible text
        filled_details_latin1 = convert_to_latin1_compatible(filled_details)
        parts = filled_details_latin1.split("MISSING INFORMATION")
        filled_form = parts[0].strip()[:-4]
        missing_info = "MISSING INFORMATION\n" + parts[1].strip() if len(parts) > 1 else "No missing information"
        st.subheader('Missing Information')
        st.write(missing_info)        

        # Convert the filled details to PDF
        pdf = MarkdownPdf()
        pdf.add_section(Section(filled_form, toc=False))
        pdf.save('filled_form_details.pdf')
        with open('filled_form_details.pdf', "rb") as pdf_file:
            st.download_button(
                label="Download Filled Form Details as PDF",
                data=pdf_file,
                file_name="filled_form_details.pdf",
                mime="application/pdf"
            )

