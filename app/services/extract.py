import docx
import PyPDF2


def extract_questions_from_pdf(file_path):
    """Extrai perguntas de um arquivo PDF"""
    questions = []
    try:
        with open(file_path, 'rb') as f:
            pdf = PyPDF2.PdfReader(f)
            for page_num in range(len(pdf.pages)):
                page = pdf.pages[page_num]
                text = page.extract_text()
                questions.append(text)
          
    except Exception as e:
        print(f"Erro ao extrair perguntas do PDF: {e}")
    
    return questions

def extract_questions_from_docx(file_path):
    """Extrai perguntas de um arquivo DOCX"""
    questions = []
    try:
        doc = docx.Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        questions.append(text)
     
    except Exception as e:
        print(f"Erro ao extrair perguntas do DOCX: {e}")
    
   
    return questions

def extract_questions(file_path):
    """Extrai perguntas de um arquivo baseado em sua extensão"""
    ext = file_path.rsplit('.', 1)[1].lower()
    
    if ext == 'pdf':
        return extract_questions_from_pdf(file_path)
    elif ext in ['docx', 'doc']:
        return extract_questions_from_docx(file_path)
    else:
        return []
