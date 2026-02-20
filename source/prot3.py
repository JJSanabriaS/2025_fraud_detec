import PyPDF2

import timeit


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


start = timeit.timeit()
texto=extract_text_from_pdf('test1.pdf')
print(texto)
end = timeit.timeit()
print(end - start)
