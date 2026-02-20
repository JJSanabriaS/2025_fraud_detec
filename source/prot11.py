import pdfplumber
import timeit

start = timeit.timeit()
with pdfplumber.open(r'test3.pdf') as pdf:
    first_page = pdf.pages[0]
    print(first_page.extract_text())

end = timeit.timeit()
print(end - start)
