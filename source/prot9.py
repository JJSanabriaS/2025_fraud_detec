import PyPDF2
import timeit

start = timeit.timeit()
pdf_file = open('test3.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
page = read_pdf.getPage(0)
page_content = page.extractText()
print(page_content.encode('utf-8'))
end = timeit.timeit()
print(end - start)
