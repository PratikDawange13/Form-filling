import streamlit as st
import google.generativeai as genai
import PyPDF2
from fpdf import FPDF
import unicodedata
import pdfkit
import markdown2
from test import extract_text_from_pdf
import os
from dotenv import load_dotenv
from markdown_pdf import MarkdownPdf, Section
load_dotenv()
# Function to extract text from the first page of a PDF
def extract_text_from_first_page(pdf_file):
    try:
        reader = PyPDF2.PdfReader(pdf_file)
        first_page = reader.pages[0]
        text = first_page.extract_text()
        if text:
            return text
        else:
            raise ValueError("No text found on the first page.")
    except Exception as e:
        st.error(f"Error extracting text: {e}")
        return None

# Function to convert text to be latin-1 compatible
def convert_to_latin1_compatible(text):
    # Replace the en-dash with a hyphen
    text = text.replace('\u2013', '-')
    text = text.replace('\u2019', '-')
    text = text.replace('\u201c', '-')
    
    
    # Normalize and encode to latin-1, ignoring unsupported characters
    text = unicodedata.normalize('NFKD', text).encode('latin-1', 'ignore').decode('latin-1')
    
    return text

api_key = os.getenv("api_key")    
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Streamlit app
st.title('Visa Form Filling')

st.header('Upload Questionnaire and Form')
uploaded_questionnaire = st.file_uploader("Upload Questionnaire PDF", type="pdf")
uploaded_form = st.file_uploader("Upload Form PDF", type="pdf")

if uploaded_questionnaire is not None and uploaded_form is not None:
    if st.button('Generate Filled Form'):
        encodedpdf1 = extract_text_from_pdf(uploaded_questionnaire.read())
        encodedpdf2 = extract_text_from_pdf(uploaded_form.read())

        prompt1 = """Please go through all the information provided below for a person"""
        prompt2 = """Fill out the following form using the provided client information. Leave fields blank if the information is not available. After completing the form, list all missing information under the heading "MISSING INFORMATION". Use proper line breaks and markdown formatting in response """
        
        # Generate content using the Generative Model
        response = model.generate_content([prompt1, encodedpdf1, prompt2, encodedpdf2])

        # Resolve the response
        response.resolve()
        filled_details = response.text

        # Convert to latin-1 compatible text
        filled_details_latin1 = convert_to_latin1_compatible(filled_details)
        #print(type(filled_details_latin1))
        # print("WHOLE FILLED DETAILS", filled_details)
        parts = filled_details_latin1.split("MISSING INFORMATION")
        # print("PARTS from the filled details",parts)
        # filled_form = parts[0].replace('\u2019', '-')
        # filled_form = filled_form.replace('\u201c', '-')
        filled_form = parts[0].strip()[:-4]
        #print(type(filled_form))

        # filled_form_formatted=convert_to_latin1_compatible(filled_form)
        # print("FILLED FORM", filled_form_formatted)
        missing_info = "MISSING INFORMATION\n" + parts[1].strip() if len(parts) > 1 else "No missing information"
        # print("MISSING INFO TEXT",missing_info)
        st.subheader('Missing Information')
        st.write(missing_info)        

        # Convert the filled details to PDF
        pdf = MarkdownPdf()
        #print("created pdf object")
        pdf.add_section(Section(filled_form, toc=False))
        # pdf.add_section(Section(filled_form, toc=False))
        #print("added a section")
        pdf.save('filled_form_details.pdf')
        #print("saved the pdf")
        with open('filled_form_details.pdf', "rb") as pdf_file:
            st.download_button(
                label="Download Filled Form Details as PDF",
                data=pdf_file,
                file_name="filled_form_details.pdf",
                mime="application/pdf"
            )