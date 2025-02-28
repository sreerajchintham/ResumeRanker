import fitz
import docx
import os

def xtrct_frm_pdf(file_path):
    pdf = fitz.open(file_path)
    text = "\n".join([page.get_text('text') for page in pdf])
    return text
# xtrct_frm_pdf("ResumeRanker/Sreeraj_DA.pdf")
def xtrct_frm_docx(file_path):
    doc = docx.Document(file_path)
    
    text = "\n".join([para.text for para in doc.paragraphs])
    print(text)
    return text

# xtrct_frm_docx("ResumeRanker/ACC_RESUME_TEMPLATE.docx")

def opener(file_path):
    if file_path[-3:] =="pdf" :
        print("pdf")
        xtrct_frm_pdf(file_path=file_path)
    elif file_path[-4:] == "docx":
        print("docx")
        xtrct_frm_docx(file_path)
    else:
        print("neither")
        return "Incorrect File Format 'pdf' and 'docx' only"

print(opener("ResumeRanker/ACC_RESUME_TEMPLATE.docx"))
