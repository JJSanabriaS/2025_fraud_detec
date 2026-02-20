import pdfplumber
import timeit
def extract_pdf(pdf_path):
    linesOfFile = []
    with pdfplumber.open(pdf_path) as pdf:
        for pdf_page in pdf.pages:
            single_page_text = pdf_page.extract_text()
            # Process the extracted text as needed
            linesOfFile.append(single_page_text)
    return linesOfFile

start = timeit.timeit()
extract_pdf('test3.pdf')
end = timeit.timeit()
print(end - start)
